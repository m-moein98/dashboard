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
    """
        This API receives plain request, gives the status of the user who requested
    """

    def get(self, request):
        try:
            isAuthenticated = request.user.is_authenticated

            if isAuthenticated:
                return Response({'success': 'user authenticated'})
            else:
                return Response({'error': 'user not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'error': 'something went wrong while checking authentication status'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    """
        This API receives signup data, creates the user and logs in with the created user
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data

            username = data['username']
            password = data['password']
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'password must be more than 6 digits'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user = User.objects.create_user(
                        username=username, password=password)
                    user.save()
                    user = User.objects.get(username=username)
                    UserProfile.objects.create(
                        user=user, first_name='', last_name='', phone='', city='')
                    return Response({'success': 'user created successfully'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'something went wrong while signup'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    """
        This receives username and password, logs in
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return Response({'success': 'user auhtneticated'})
            else:
                return Response({'error': 'user not auhtneticated'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'error': 'something went wrong at login'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
        This APi receives plain request, logs out the user who requested
    """

    def post(self, request):
        try:
            auth.logout(request)
            return Response({'success': 'logged out'})
        except:
            return Response({'error': 'something went wrong while logging out'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteAcountView(APIView):
    """
        The API receives plain request, deletes the user who requested
    """

    def delete(self, request):
        user = request.user
        try:
            user = user.objects.filter(id=user.id).delete()
            return Response({'success': 'user deleted successfully'})
        except:
            return Response({'error': 'something went wrong while trying to delete user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    """
        The API reciesves plain request, sets the CSRFToken
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'success': 'CSRF cookie set'})


class GetUsersView(APIView):
    """
        The API receives request from ADMIN, returns list of all users
    """
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        try:
            users = User.objects.all()
            users = UserSerializer(users, many=True)
            return Response({'success': users.data})
        except:
            return Response({'error': 'something went wrong while trying to get users list'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
