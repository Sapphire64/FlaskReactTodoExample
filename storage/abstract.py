class AbstractToDoStorageProvider(object):

    def get_item(self, user, id_):
        """ Returns item with specific ID

        :user: owner of the ToDo item
        :id_: id of ToDo item in database
        :return: dict() of requested item
            {'id', 'data', 'is_active'} or None
        """

    def get_items(self, user):
        """ Returns all items for specific user

        :user: owner of the ToDo item
        :return: list() of requested items (dicts)
            [{'id', 'data', 'is_active'},
             {'id', 'data', 'is_active'}, ...]
        """

    def create_item(self, user, data):
        """ Inserts ToDO data body and returns complete item.

        :user: owner of the ToDo item
        :data: body of the todo item
        :return: dict() of inserted item
            {'id', 'data', 'is_active'}
        """
        pass

    def update_item(self, user, id_, new_data):
        """ Updates item for id_

        :user: owner of the ToDo item
        :id_: id of ToDo item in database
        :new_data: data to be inserted in id_
        :return: dict() of updated item
            {'id', 'data', 'is_active'}
        """
        pass

    def remove_item(self, usr, id_):
        """ Removes specific ToDo from the database

        :user: owner of the ToDo item
        :id_: id of ToDo to be removed
        :return: None
        """
        pass