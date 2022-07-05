from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from .models import ProfileModel

UserModel=get_user_model()

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel

