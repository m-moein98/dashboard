from .test_setup import TestSetUp
from django.contrib import auth
from django.contrib.auth.models import User
from django.test import Client

class TestViews(TestSetUp):
    def test_user_can_register_with_no_data(self):
        res = self.client.post(self.register_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'error', res_message)
    
    def test_user_can_register_with_incorrect_data(self):
        res = self.client.post(self.register_url,self.incorrect_signup_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'error', res_message)
    
    def test_user_can_register_with_correct_data(self):
        res = self.client.post(self.register_url,self.correct_signup_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'success', res_message)


    def test_user_can_login_with_no_data(self):
        res = self.client.post(self.login_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'error', res_message)
    
    def test_user_can_login_with_wrong_data(self):
        res = self.client.post(self.login_url,self.incorrect_signin_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'error', res_message)

    def test_user_can_login_with_correct_data(self):
        self.user = User.objects.create_user(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        res = self.client.post(self.login_url,self.correct_signin_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'success', res_message)


    def test_user_can_logout_with_incorrect_credentials(self):
        res = self.client.post(self.logout_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation

        self.assertEqual(res_type, 'detail', res_message) # detail means no credentials or invalid credentials

    def test_user_can_logout_with_correct_credentials(self):
        self.user = User.objects.create_user(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        self.client.login(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        res = self.client.post(self.logout_url,self.correct_signin_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        self.assertEqual(res_type, 'success', res_message)
    

    def test_user_can_check_auth_status_with_incorrect_credentials(self):
        res = self.client.post(self.authenticated_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'detail', res_message) # detail means no credentials or invalid credentials
        
    def test_user_can_check_auth_status_with_correct_credentials(self):
        self.user = User.objects.create_user(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        self.client.login(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])

        res = self.client.get(self.authenticated_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'success', res_message)
    
    
    def test_anyone_can_get_csrf_token(self):
        res = self.client.get(self.csrf_cookie_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'success', res_message)


    def test_admin_can_get_users_list_with_incorrect_credentials(self):
        self.user = User.objects.create_user(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        self.client.login(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])

        res = self.client.post(self.get_users_url,self.correct_signin_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'detail', res_message) # detail means you dont have permission
        
    def test_admin_can_get_users_list_with_correct_credentials(self):
        self.user = User.objects.create_user(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'], is_staff=True)
        self.client.login(username=self.correct_signin_data['username'], password=self.correct_signin_data['password'])
        
        # is_superuser
        res = self.client.get(self.get_users_url,self.correct_signin_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'success', res_message)