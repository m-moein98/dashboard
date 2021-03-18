from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestSetUp(APITestCase):
    def setUp(self):
        self.get_profiles_url = reverse('profile')
        self.update_url = reverse('update')
        self.signup_data = {
            'username':'SomeRandomUsername',
            'password':'Password4Test',
        }
        self.signin_data = {
            'username':'SomeRandomUsername',
            'password':'Password4Test',
        }
        self.profile_data = {
            'user':User.objects.create_user(
                username=self.signup_data['username'],
                password=self.signup_data['password']
            ),
            'first_name':'john',
            'last_name':'due',
            'phone':'+19100000000',
            'city':'berlin'
        }

        return super().setUp()
    def tearDown(self):
        return super().tearDown()