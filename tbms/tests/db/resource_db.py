from tests.db import resource_db_stubs as stub

class ResourceDB:

    @staticmethod
    def create(item, values):
        """
        Description: Adds a new item to the database
        :param item: A string specifying which class that is to be added
        :param values: A dictionary with the values that are to be added to
            the row corresponding to the new item
        :return: The id of the item that was created in the database
        """
        return stub.create(item, values)

    @staticmethod
    def read(item, item_id=None):
        """
        Retrieves the specified item from the database by the identifier
        provided.
        :param item: A string of the class that the caller wants to get from
            the db
        :param item_id: An identifier used to retrieve the item from the
            database.
        :return: A dictionary of the item that was requested.  If the item
            was not found in the database it should return an empty dictionary.
        """
        return stub.read(item, item_id)

    @staticmethod
    def update(item, item_id, values):
        """
        Updates a specific row of the table with new information.
        :param item: A string of the name of the class that is going to be
            updated.
        :param item_id: Identifier of which item is to be updated
        :param values: A dictionary of values that the caller wants to changed
            in the table
        :return: A boolean if the update was successful or not
        """
        return stub.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Deletes the item with the specified id from the database
        :param item: String of the class that the caller wants to delete.
        :param item_id: Identifier of the item that the caller wants to delete.
        :return: A boolean if the deletion was successful or not
        """
        return stub.delete(item, item_id)