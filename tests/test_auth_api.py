import unittest
from app import create_app, db
from .base import BaseTestCase
from app.models.User import User


class AuthApiTestCase(unittest.TestCase):
    """Auth API Tests."""

    def test_registered_user_login(self):
        pass

    def test_non_registered_user_login(self):
        pass

    def test_logout_access(self):
        pass

    def test_logout_refresh(self):
        pass

    def test_token_refresh(self):
        pass
