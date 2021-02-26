from django.urls import path
from .views import GetUserProfileView, UpdateProfileView
urlpatterns = [
    path('profile', GetUserProfileView.as_view()),
    path('update', UpdateProfileView.as_view()),
]