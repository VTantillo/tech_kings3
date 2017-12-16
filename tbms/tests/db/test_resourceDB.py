from unittest import TestCase
from tests.db.resource_db import ResourceDB as Resource


class TestResourceDB(TestCase):
    pass


class TestCreate(TestResourceDB):

    def test_valid_ref(self):
        valid_ref = {'name': 'res1', 'file_location': 'c:/home',
                     'type': 'pdf'}
        item_id = Resource.create("reference material", valid_ref)
        self.assertEquals(item_id, 1)

    def test_valid_survey(self):
        valid_survey = {'name': 'sur1', 'file_location': 'c:/home',
                        'completed': False, 'user_id': 2}
        item_id = Resource.create("survey", valid_survey)
        self.assertEquals(item_id, 2)

    def test_invalid_item(self):
        valid_survey = {'name': 'sur1', 'file_location': 'c:/home',
                        'user_id': 2}
        item_id = Resource.create("user", valid_survey)
        self.assertEquals(item_id, -3)

    def test_invalid_ref(self):
        invalid = {'user': 'derp'}
        item_id = Resource.create("reference material", invalid)
        self.assertEquals(item_id, -1)

    def test_invalid_survey(self):
        invalid = {'user': 'derp'}
        self.assertEquals(Resource.create("survey", invalid), -2)
