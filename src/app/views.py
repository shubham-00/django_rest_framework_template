from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from .models import BlogPost
from .serializers import BlogPostSerializer, RegistrationSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(["GET"])
def api_detail_blog_view(request, slug):
    print("Host:", request.headers.get("Host"))
    try:
        blog_post = BlogPost.objects.get(slug=slug)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


@api_view(["PUT"])
def api_update_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = BlogPostSerializer(blog_post, request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)

        return Response({"error": "error"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def api_delete_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = blog_post.delete()

        data = {}
        if operation:
            data["success"] = "delete successfull"
        else:
            data["failure"] = "delete failed"

        return Response(data=data)


@api_view(["POST"])
# @parser_classes([MultiPartParser, FormParser, JSONParser])
def api_create_blog_view(request):
    account = User.objects.get(pk=1)

    blog_post = BlogPost(author=account)

    if request.method == "POST":
        serializer = BlogPostSerializer(blog_post, data=request.data)

        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def api_registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Successfully registered a new user!"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = Token.objects.get(user=account).key
        else:
            data = serializer.errors

        return Response(data)


@api_view(["POST"])
def api_login_view(request):
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        data = {}

        account = authenticate(
            username=serializer.initial_data.get("username"),
            password=serializer.initial_data.get("password"),
        )

        if account:
            data["token"] = Token.objects.get(user=account).key
        else:
            data["error"] = "Invalid username or password!"

        return Response(data)
