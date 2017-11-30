"""
Salamah said to try and make it so that this module just has 4 methods that
everyone can use.
"""
import db.db_workshop as workshop
import db.db_user as user
import db.db_network as network
import db.db_resources as resources


class WorkshopDB:
    @staticmethod
    def get(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        data = workshop.get(item, item_id)
        return data

    @staticmethod
    def add(item, values):
        """
        Description:
        :param item:
        :param values:
        :return:
        """
        new_id = workshop.add(item, values)
        return new_id

    @staticmethod
    def update(item, item_id, values):
        """
        Description:
        :param item:
        :param item_id:
        :param values:
        :return:
        """
        # need to check whether or not the values dict is empty first
        workshop.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        workshop.delete(item, item_id)


class UserDB:
    @staticmethod
    def get(item, item_id):
        """

        :param item:
        :param item_id:
        :return:
        """
        data = user.get(item, item_id)
        return data

    @staticmethod
    def add(item, values):
        """
        Description:
        :param item:
        :param values:
        :return:
        """
        return user.add(item, values)

    @staticmethod
    def update(item, item_id, values):
        """
        Description:
        :param item:
        :param item_id:
        :param values:
        :return:
        """
        user.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        user.delete(item, item_id)


class NetworkDB:
    @staticmethod
    def get(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        data = network.get(item, item_id)
        return data

    @staticmethod
    def add(item, values):
        """
        Description:
        :param item:
        :param values:
        :return:
        """
        return network.add(item, values)

    @staticmethod
    def update(item, item_id, values):
        """
        Description:
        :param item:
        :param item_id:
        :param values:
        :return:
        """
        network.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        network.delete(item, item_id)


class ResourceDB:
    @staticmethod
    def get(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        data = resources.get(item, item_id)
        return data

    @staticmethod
    def add(item, values):
        """
        Description:
        :param item:
        :param values:
        :return:
        """
        return resources.add(item, values)

    @staticmethod
    def update(item, item_id, values):
        """
        Description:
        :param item:
        :param item_id:
        :param values:
        :return:
        """
        resources.update(item, item_id, values)

    @staticmethod
    def delete(item, item_id):
        """
        Description:
        :param item:
        :param item_id:
        :return:
        """
        resources.delete(item, item_id)
