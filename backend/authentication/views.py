from rest_framework.views import APIView
from rest_framework import permissions
from dashboard.models import UserProfile
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib import auth
from .serializers import UserSerializer


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            isAuthenticated = User.is_authenticated

            if isAuthenticated:
                return Response({'isAuthenticated':'success'})
            else:
                return Response({'isAuthenticated':'error'})
        except:
            return Response({'error':'something went wrong while checking authentication status'})

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
                        return Response({'error':'password must be more than 6 digits'})
                    else:
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        user = User.objects.get(username=username)
                        user_profile = UserProfile.objects.create(user=user, first_name='', last_name='', phone='', city='')
                        return Response({'success':'user created successfully'})
            else:
                return Response({'error':'Password doesnt match'})
        except:
            return Response({'error':'something went wrong while signup'})

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
                return Response({'error':'user not auhtneticated'})
        except:
            return Response({'error':'something went wrong at login'})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            auth.logout(request)
            return Response({'success':'logged out'})
        except:
            return Response({'error':'something went wrong while logging out'})

class DeleteAcountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user
        try:
            user = user.objects.filter(id=user.id).delete()
            return Response({'success','user deleted successfully'})
        except:
            return Response({'error','something went wrong while trying to delete user'})

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        return Response({'success':'CSRF cookie set'})

class GetUsersView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)