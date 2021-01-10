from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_create_blog_view,
    api_delete_blog_view,
    api_registration_view,
    api_login_view,
    ApiBlogListView,
    profile_update_view,
    profile_detail_view,
)


app_name = "app"


urlpatterns = [
    path("", ApiBlogListView.as_view(), name="home"),
    path("create/", api_create_blog_view, name="create"),
    path("register/", api_registration_view, name="register"),
    # path("login/", obtain_auth_token, name="login"),
    path("login/", api_login_view, name="login"),
    path("profile/", profile_detail_view, name="profile"),
    path("profile/update/", profile_update_view, name="profile-update"),
    path("<slug>/", api_detail_blog_view, name="detail"),
    path("<slug>/update/", api_update_blog_view, name="update"),
    path("<slug>/delete/", api_delete_blog_view, name="delete"),
]
