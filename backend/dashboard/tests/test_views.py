from .test_setup import TestSetUp
from django.contrib.auth.models import User
from dashboard.models import UserProfile


class TestViews(TestSetUp):
    def test_user_can_update_profile_with_incorrect_data(self):
        res = self.client.put(self.update_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'detail', res_message) # detail means there is no credentials

    def test_user_can_update_profile_with_correct_data(self):
        self.profile_data['user'] = self.profile_data['user'].id
        self.client.login(username=self.signin_data['username'], password=self.signin_data['password'])
        UserProfile.objects.create(user=User.objects.get(id=self.profile_data['user']), first_name='', last_name='', phone='', city='')

        res = self.client.put(self.update_url, self.profile_data, format="json")
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'profile', res_message)

    
    def test_user_can_get_profile_view_with_incorrect_credentials(self):
        res = self.client.get(self.get_profiles_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'detail', res_message) # detail means there is no credentials

    def test_user_can_get_profile_view_with_correct_credentials(self):
        self.user = self.profile_data['user']
        self.client.login(username=self.signin_data['username'], password=self.signin_data['password'])
        self.user_profile = UserProfile.objects.create(
            user=self.profile_data['user'],
            first_name=self.profile_data['first_name'],
            last_name=self.profile_data['last_name'],
            phone=self.profile_data['phone'],
            city=self.profile_data['city']
        )
        res = self.client.get(self.get_profiles_url)
        res_type = list(res.data.keys())[0] # it can be error or success
        res_message = list(res.data.values())[0] # it explaines the situation
        
        self.assertEqual(res_type, 'profile', res_message)