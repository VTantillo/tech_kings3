from unittest import TestCase
from tests.db.user_db import UserDB as User


class TestUserDB(TestCase):
    pass


class TestDelete(TestUserDB):

    def test_valid(self):
        self.assertTrue(User.delete("user", 2))

    def test_invalid_item(self):
        self.assertFalse(User.delete("server", 3))

    def test_invalid_neg_id(self):
        self.assertFalse(User.delete("credentials", -1))

    def test_invalid_pos_id(self):
        self.assertFalse(User.delete("user", 30))
