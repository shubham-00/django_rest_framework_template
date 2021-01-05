from django.urls import path
from .views import api_detail_blog_view


app_name = "app"


urlpatterns = [
    path("<slug>/", api_detail_blog_view, name="detail"),
]
