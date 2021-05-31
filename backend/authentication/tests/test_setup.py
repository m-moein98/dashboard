from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    """
    This class provides test informations
    """

    def setUp(self):
        self.authenticated_url = reverse("authenticated")
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.delete_url = reverse("delete")
        self.csrf_cookie_url = reverse("csrf_cookie")
        self.get_users_url = reverse("get_users")

        self.correct_signup_data = {
            'username': 'SomeRandomUsername',
            'password': 'Password4Test'
        }

        # credentials are wrong
        self.incorrect_signin_data = {
            'username': 'SomeRandomUsername',
            'password': 'Password4Test9754654',
        }

        self.correct_signin_data = {
            'username': 'SomeRandomUsername',
            'password': 'Password4Test',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
