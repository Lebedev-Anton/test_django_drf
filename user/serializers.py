from rest_framework import serializers

from user.models import User, UserPhoto


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ['user', 'photo']


class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'http://127.0.0.1:8000/' + str(value.photo)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )
    photo = TrackListingField(read_only=True)

    def create(self, validated_data) -> User:
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password'))
        return user

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'birthday', 'gender', 'password', 'photo']

