from .test_setup import TestSetUp
from ..models import UserProfile
from ..serializers import UserProfileSerializer
from django.contrib.auth.models import User


class TestSerializers(TestSetUp):
    def test_get_user_list(self):
        user_profile = UserProfile.objects.create(
            user=self.profile_data['user'],
            first_name=self.profile_data['first_name'],
            last_name=self.profile_data['last_name'],
            phone=self.profile_data['phone'],
            city=self.profile_data['city']
        )
        serialized_data = UserProfileSerializer(user_profile)

        self.assertEqual(User.objects.get(id=serialized_data.data['user']), self.profile_data['user'], 'serializer doesnt serialize user')
        self.assertEqual(serialized_data.data['first_name'], self.profile_data['first_name'], 'serializer doesnt serialize first name')
        self.assertEqual(serialized_data.data['last_name'], self.profile_data['last_name'], 'serializer doesnt serialize last name')
        self.assertEqual(serialized_data.data['phone'], self.profile_data['phone'], 'serializer doesnt serialize phone number')
        self.assertEqual(serialized_data.data['city'], self.profile_data['city'], 'serializer doesnt serialize city')