from django.urls import path
from .views import SignupView, GetCSRFToken, CheckAuthenticatedView, LoginView, LogoutView, DeleteAcountView, GetUsersView


urlpatterns = [
    path('authenticated', CheckAuthenticatedView.as_view(), name="authenticated"),
    path('register', SignupView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('delete', DeleteAcountView.as_view(), name="delete"),
    path('csrf_cookie', GetCSRFToken.as_view(), name="csrf_cookie"),
    path('get_users', GetUsersView.as_view(), name="get_users"),
]
