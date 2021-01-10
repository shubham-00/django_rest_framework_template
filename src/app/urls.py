from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_create_blog_view,
    api_delete_blog_view,
    api_registration_view,
    api_login_view,
)


app_name = "app"


urlpatterns = [
    path("create/", api_create_blog_view, name="create"),
    path("register/", api_registration_view, name="register"),
    # path("login/", obtain_auth_token, name="login"),
    path("login/", api_login_view, name="login"),
    path("<slug>/", api_detail_blog_view, name="detail"),
    path("<slug>/update/", api_update_blog_view, name="update"),
    path("<slug>/delete/", api_delete_blog_view, name="delete"),
]
