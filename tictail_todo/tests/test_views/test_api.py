import unittest
import json

from random import choice, randint
from uuid import uuid4

# App imports
from tictail_todo.app import app
from tictail_todo.storage.inmemory_dict import STORAGE
from tictail_todo.views import api


class TodoApiTestCase(unittest.TestCase):

    def setUp(self):
        # Enforcing memory-based engine for integration tests
        app.config['STORAGE_ENGINE'] = \
            'storage.inmemory_dict.InMemoryDictToDoStorageProvider'
        self.storage = STORAGE
        self.app = app.test_client()

    def tearDown(self):
        STORAGE.clear()

    def test_submit_todo(self):
        todo_data = {'data': uuid4().hex}
        expected_stored_todo_data = \
            dict(todo_data.items() + {'is_active': True}.items())

        response = self.app.post('/todos/', data=json.dumps(todo_data),
                                 headers={'content-type': 'application/json'})
        response_data = json.loads(response.data)

        self.assertDictContainsSubset(
            expected_stored_todo_data,
            response_data
        )
        self.assertIsNotNone(response_data.get('id'),
                             "id should be present in body")

        # Checking DB entry
        self.assertEqual(
            self.storage[api.USER_ID].get(response_data.get('id')),
            expected_stored_todo_data
        )

    def test_retrieve_all_todos(self):
        expected_data = []
        # Inserting entries to db
        for _ in xrange(10):
            id_ = uuid4().hex
            data = {'data': uuid4().hex, 'is_active': choice([True, False])}

            expected_data.append(
                dict({'id': id_}.items() + data.items())
            )
            self.storage[api.USER_ID][id_] = data

        response = self.app.get('/todos/')
        response_data = json.loads(response.data)

        self.assertListEqual(
            sorted(expected_data),
            sorted(response_data)
        )

    def test_retrieve_one_todo(self):
        # Inserting entries to db
        for _ in xrange(10):
            id_ = randint(0, 10000000)
            data = {'data': uuid4().hex, 'is_active': choice([True, False])}
            self.storage[api.USER_ID][id_] = data

        # Choosing item to retrieve
        requested_id = choice(self.storage[api.USER_ID].keys())
        expected_json_body = dict(
            {'id': requested_id}.items() +
            self.storage[api.USER_ID][requested_id].items()
        )

        response = self.app.get(u'/todos/{}'.format(requested_id))
        response_data = json.loads(response.data)

        self.assertDictEqual(
            response_data,
            expected_json_body
        )

    def test_update_item(self):
        id_ = randint(0, 10000000)
        data = {'data': uuid4().hex, 'is_active': choice([True, False])}
        self.storage[api.USER_ID][id_] = data

        updated_todo_data = dict(
            data.items() + {'is_active': not data.get('is_active')}.items()
        )
        expected_response = dict(
            updated_todo_data.items() + {'id': id_}.items()
        )

        response = self.app.put(u'/todos/{}'.format(id_),
                                data=json.dumps(updated_todo_data),
                                headers={'content-type':'application/json'})
        response_data = json.loads(response.data)

        self.assertDictEqual(
            response_data,
            expected_response
        )

        # Validating DB value
        self.assertDictEqual(
            self.storage[api.USER_ID][id_],
            updated_todo_data
        )

    def test_remove_item(self):
        id_ = randint(0, 10000000)
        data = {'data': uuid4().hex, 'is_active': choice([True, False])}
        self.storage[api.USER_ID][id_] = data

        response = self.app.delete(u'/todos/{}'.format(id_))
        response_data = json.loads(response.data)

        self.assertIsNone(response_data)
        self.assertTrue(
            id_ not in self.storage[api.USER_ID].keys()
        )