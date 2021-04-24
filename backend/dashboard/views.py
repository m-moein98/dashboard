from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from .models import UserProfile
from .serializers import UserProfileSerializer


class UpdateProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username= user.username
            data = self.request.data
            first_name = data['first_name']
            last_name = data['last_name']
            phone = data['phone']
            city = data['city']

            user = User.objects.get(id=user.id)
            UserProfile.objects.filter(user=user).update(first_name=first_name,last_name=last_name, phone=phone,city=city)
            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile':user_profile.data,'username':str(user.username)})
        except:
            return Response({'error':'something unexpected happend while trying to update the profile'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUserProfileView(APIView):
    def get(self, requet, format=None):
        try:
            user = self.request.user
            username = user.username

            user_profile = UserProfile.objects.filter(user=user)
            user_profile = UserProfileSerializer(user_profile, many=True)

            return Response({'profile':user_profile.data,'username':str(username)})
        except:
            return Response({'error':'profile list doesnt exists'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)