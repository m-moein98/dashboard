from django.urls import path
from .views import GetUserProfileView, UpdateProfileView


urlpatterns = [
    path('profile', GetUserProfileView.as_view(), name="profile"),
    path('update', UpdateProfileView.as_view(), name="update"),
]
