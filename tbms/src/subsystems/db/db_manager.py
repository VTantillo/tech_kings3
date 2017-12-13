"""
Interface for the rest of the system to the database
"""

import db_workshop as workshop
import db_user as user
import db_network as network
import db_resources as resources


class WorkshopDB:

    @staticmethod
    def create(item, values):
        """
        Adds a new item to the database
        :param item: A string specifying which class that is to be added
        :param values: A dictionary with the values that are to be added to
            the row corresponding to the new item
        :return: The id of the item that was created in the database
        """
        new_id = workshop.create(item, values)
        return new_id

    @staticmethod
    def read(item, item_id=None):
        """
        Retrieves the specified item from the database by the identifier
        provided.
        :param item: A string of the class that the caller wants to get from
            the db
        :param item_id: An identifier used to retrieve the item from the
            database.  In the case of the workshop, it should be an integer
        :return: A dictionary of the item that was requested.  If the item
            was not found in the database it should return an empty dictionary.
        """
        data = workshop.read(item, item_id)
        return data

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
        # need to check whether or not the values dict is empty first
        return workshop.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Deletes the item with the specified id from the database
        :param item: String of the class that the caller wants to delete.
        :param item_id: Identifier of the item that the caller wants to delete.
        :return: A boolean if the deletion was successful or not
        """
        return workshop.delete(item, item_id)


class UserDB:

    @staticmethod
    def create(item, values):
        """
        Adds a new item to the database
        :param item: A string specifying which class that is to be added
        :param values: A dictionary with the values that are to be added to
            the row corresponding to the new item
        :return: The id of the item that was created in the database
        """
        return user.create(item, values)

    @staticmethod
    def read(item, item_id=None):
        """
        Retrieves the specified item from the database by the identifier
        provided.
        :param item: A string of the class that the caller wants to get from
            the db
        :param item_id: An identifier used to retrieve the item from the
            database. For the user, a special case is getting the
            credentials, so the identifier could be a string as well as int
        :return: A dictionary of the item that was requested.  If the item
            was not found in the database it should return an empty dictionary.
        """
        return user.read(item, item_id)

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
        return user.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Deletes the item with the specified id from the database
        :param item: String of the class that the caller wants to delete.
        :param item_id: Identifier of the item that the caller wants to delete.
        :return: A boolean if the deletion was successful or not
        """
        return user.delete(item, item_id)


class NetworkDB:

    @staticmethod
    def create(item, values):
        """
        Description: Adds a new item to the database
        :param item: A string specifying which class that is to be added
        :param values: A dictionary with the values that are to be added to
            the row corresponding to the new item
        :return: The id of the item that was created in the database
        """
        return network.create(item, values)

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
        return network.read(item, item_id)

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
        return network.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Deletes the item with the specified id from the database
        :param item: String of the class that the caller wants to delete.
        :param item_id: Identifier of the item that the caller wants to delete.
        :return: A boolean if the deletion was successful or not
        """
        return network.delete(item, item_id)


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
        return resources.create(item, values)

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
        return resources.read(item, item_id)

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
        return resources.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Deletes the item with the specified id from the database
        :param item: String of the class that the caller wants to delete.
        :param item_id: Identifier of the item that the caller wants to delete.
        :return: A boolean if the deletion was successful or not
        """
        return resources.delete(item, item_id)
