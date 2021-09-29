from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from rest_framework import serializers
from users.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff',
                   'groups', 'user_permissions',)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ('id',)

    def get_user(self, obj):
        return UserSerializer(obj.user, many=False).data


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    user_type = serializers.IntegerField()

    def validate(self, data):
        email = data['email']

        if(User.objects.filter(email=email).exists()):
            raise serializers.ValidationError("This email is already registered")

        return data

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(email, password)
        user.save()
        profile = Profile.objects.get(user=user)
        profile.user_type = validated_data['user_type']
        profile.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if not user.is_active:
                raise serializers.ValidationError("Admin deactivated your account")
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Email is not register")

        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError("Please check email and password")
        if not user.profile.email_varified:
            raise serializers.ValidationError('Please varify your email address')

        return user
