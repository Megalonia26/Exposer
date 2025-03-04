from django.urls import path

from . import views as profiles_views

urlpatterns = [
    path("", profiles_views.UserProfiles, name="user-profiles")
]
