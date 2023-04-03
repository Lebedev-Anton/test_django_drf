import os

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from PIL import Image


class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, first_name: str, last_name: str, **kwargs) -> AbstractBaseUser:
        if not email:
            raise ValueError('The given email must be set')

        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, first_name: str, last_name: str) -> AbstractBaseUser:
        if not email:
            raise ValueError('The given email must be set')

        if not password:
            raise ValueError('The given password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        male = 'm', 'male'
        female = 'f', 'female'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_username(self) -> str:
        """Return the username for this User."""
        return self.get_full_name()

    def get_full_name(self) -> str:
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        return str(self.first_name)


def upload_file(instance: models.Model, filename: str) -> str:
    path = 'static/update/'

    try:
        os.remove(path + filename)
    except FileNotFoundError:
        pass
    return path + filename


class UserPhoto(models.Model):
    photo = models.FileField(upload_to=upload_file, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='photo')

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.photo.name is not None:
            img = Image.open(self.photo.path)
            w, h = img.size
            img.crop((0, 150, w, h - 150)).save(self.photo.path)
