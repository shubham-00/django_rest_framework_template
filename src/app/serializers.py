from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["title", "body", "image", "date_updated"]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        account = User(
            email=self.validated_data.get("email"), username=self.validated_data.get("username")
        )
        password = self.validated_data.get("password")
        password2 = self.validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match!"})

        account.set_password(password)
        account.save()

        return account


"""
{
"email":"test@gmail.com",
"username":"test",
"password":"testing1234",
"password2":"testing123"
}
"""


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
