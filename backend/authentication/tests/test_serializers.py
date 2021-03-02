from .test_setup import TestSetUp
from django.contrib.auth.models import User
from ..serializers import UserSerializer


class TestSerializers(TestSetUp):
    def test_get_user_list(self):
        user = User.objects.create_user(username="SomeRandomUsername4Test",password="SomePasswords4Test")
        user.save()
        created_user = User.objects.get(username="SomeRandomUsername4Test")
        serialized_data = UserSerializer(user)
        created_user.delete()
        self.assertEqual(serialized_data.data['username'], 'SomeRandomUsername4Test', 'serializer doesnt work')
