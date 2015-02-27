from collections import defaultdict

from uuid import uuid4

from tictail_todo.storage.abstract import AbstractToDoStorageProvider


STORAGE = defaultdict(dict)


class InMemoryDictToDoStorageProvider(AbstractToDoStorageProvider):

    def _build_item(self, id_, item_body):
        """ Helper method to return generated structure of item
        """
        return dict({'id': id_}.items() + item_body.items())

    def get_item(self, user, id_):
        """ Returns item with specific ID

        :user: owner of the ToDo item
        :id_: id of ToDo item in database
        :return: dict() of requested item
            {'id', 'data', 'is_active'} or None
        """
        data = STORAGE[user].get(id_)
        if data is None:
            return None
        return self._build_item(id_, data)

    def get_items(self, user):
        """ Returns all items for specific user

        :user: owner of the ToDo item
        :return: list() of requested items (dicts)
            [{'id', 'data', 'is_active'},
             {'id', 'data', 'is_active'}, ...]
        """
        user_items = STORAGE[user]
        return [
            self._build_item(id_, data)
            for id_, data in user_items.items()
        ]

    def create_item(self, user, data):
        """ Inserts ToDO data body and returns complete item.

        :user: owner of the ToDo item
        :data: body of the todo item
        :return: dict() of inserted item
            {'id', 'data', 'is_active'}
        """
        id_ = uuid4().hex
        STORAGE[user].update({id_: {'data': data, 'is_active': True}})
        return self._build_item(id_, STORAGE[user].get(id_))

    def update_item(self, user, id_, new_data_body):
        """ Updates item for id_

        :user: owner of the ToDo item
        :id_: id of ToDo item in database
        :new_data: data to be inserted in id_
        :return: dict() of updated item
            {'id', 'data', 'is_active'}
        """
        STORAGE[user][id_] = new_data_body
        return self._build_item(id_, STORAGE[user].get(id_))

    def remove_item(self, user, id_):
        """ Removes specific ToDo from the database

        :user: owner of the ToDo item
        :id_: id of ToDo to be removed
        :return: None
        """
        del STORAGE[user][id_]