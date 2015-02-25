from uuid import uuid4
from collections import defaultdict

from unittest import TestCase

from mock import patch

from storage.inmemory_dict import InMemoryDictToDoStorageProvider


MOCKED_STORAGE = defaultdict(dict)


def mocked_build_item(id_, data):
    # Please pay attention that signature of this method is not
    # following original's for output
    return [id_, data]


@patch(InMemoryDictToDoStorageProvider.__module__ + '.STORAGE', MOCKED_STORAGE)
class InMemoryDictToDoStorageProviderTest(TestCase):

    def setUp(self):
        self.user = uuid4().hex
        self.provider = InMemoryDictToDoStorageProvider()
        self.provider._build_item = mocked_build_item

    def test_create_item(self):
        target = self.provider.create_item

        data = {uuid4().hex: uuid4().hex for _ in xrange(2)}

        result1 = target(self.user, data)

        self.assertDictEqual(result1[1], {'is_active': True, 'data': data})
        self.assertDictEqual(MOCKED_STORAGE.get(self.user)[result1[0]],
                         {'is_active': True, 'data': data})

        # Checking that ID is unique
        result2 = target(self.user, data)
        self.assertNotEqual(result1[0], result2[0])

    def test_get_item(self):
        target = self.provider.get_item

        id_ = uuid4().hex
        data = {'is_active': True,
                'data': {uuid4().hex: uuid4().hex for _ in xrange(2)}}

        MOCKED_STORAGE[self.user][id_] = data

        result = target(self.user, id_)
        self.assertListEqual(
            [id_, data],
            result
        )

        # Trying with empty item
        self.assertIsNone(target(self.user, uuid4().hex))

    def test_get_items(self):
        target = self.provider.get_items

        expected_result = []

        for _ in xrange(10):
            id_ = uuid4().hex
            data = {'is_active': True,
                    'data': {uuid4().hex: uuid4().hex for _ in xrange(2)}}

            expected_result.append([id_, data])

            MOCKED_STORAGE[self.user][id_] = data

        self.assertListEqual(
            sorted(target(self.user)), sorted(expected_result)
        )

    def test_update_item(self):
        target = self.provider.update_item

        id_ = uuid4().hex
        data = {'is_active': True,
                'data': {uuid4().hex: uuid4().hex for _ in xrange(2)}}

        MOCKED_STORAGE[self.user][id_] = data

        # Replacement data for entry
        new_data = {'is_active': False,
                    'data': {uuid4().hex: uuid4().hex for _ in xrange(2)}}

        self.assertListEqual(
            target(self.user, id_, new_data),
            [id_, new_data]
        )
        self.assertEqual(
            MOCKED_STORAGE[self.user][id_],
            new_data
        )

    def test_remove_item(self):
        target = self.provider.remove_item

        id_ = uuid4().hex
        data = {'is_active': True,
                'data': {uuid4().hex: uuid4().hex for _ in xrange(2)}}

        MOCKED_STORAGE[self.user][id_] = data

        self.assertIsNone(target(self.user, id_))
        self.assertTrue(
            id_ not in MOCKED_STORAGE[self.user].keys()
        )


