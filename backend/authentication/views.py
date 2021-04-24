from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import auth
from dashboard.models import UserProfile
from .serializers import UserSerializer


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            isAuthenticated = User.is_authenticated

            if isAuthenticated:
                return Response({'success':'user authenticated'})
            else:
                return Response({'error':'user not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'error':'something went wrong while checking authentication status'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        try:
            data = self.request.data

            username = data['username']
            password = data['password']
            re_password = data['re_password']
            if re_password == password:
                if User.objects.filter(username=username).exists():
                    return Response({'error':'Username already exists'})
                else:
                    if len(password) < 6:
                        return Response({'error':'password must be more than 6 digits'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(username=username)
                        user_profile = UserProfile.objects.create(user=user, first_name='', last_name='', phone='', city='')
                        return Response({'success':'user created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'Password doesnt match'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'error':'something went wrong while signup'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            data = self.request.data
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({'success':'user auhtneticated'})
            else:
                return Response({'error':'user not auhtneticated'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'error':'something went wrong at login'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success':'logged out'})
        except:
            return Response({'error':'something went wrong while logging out'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteAcountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            user = user.objects.filter(id=user.id).delete()
            return Response({'success':'user deleted successfully'})
        except:
            return Response({'error':'something went wrong while trying to delete user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        return Response({'success':'CSRF cookie set'})

class GetUsersView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        try:
            users = User.objects.all()
            users = UserSerializer(users, many=True)
            return Response({'success':users.data})
        except:
            return Response({'error':'something went wrong while trying to get users list'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)