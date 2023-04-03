from copy import copy
from collections import OrderedDict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from user.models import User, UserPhoto


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )
    photo = serializers.FileField(required=False)

    def create(self, validated_data) -> User:
        user_data = copy(validated_data)
        if user_data.get('photo') is not None:
            del user_data['photo']
        user = User.objects.create_user(**user_data)
        user.set_password(validated_data.get('password'))
        UserPhoto.objects.update_or_create(
            user=user,
            defaults={'photo': validated_data.get('photo'), 'user': user},
        )
        return user

    def to_representation(self, instance) -> OrderedDict:
        representation = super().to_representation(instance)
        try:
            representation.__setitem__('photo', 'http://127.0.0.1:8000/' + instance.photo.photo.url)
        except (ValueError, ObjectDoesNotExist):
            return representation

        return representation

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'birthday', 'gender', 'password', 'photo']
