from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self,username, email , password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        # is_company, phone_number, profile_img ,card_id_img,commercial_record_img,country =  kwargs['phone_number'],kwargs['is_company'], kwargs['phone_number'],kwargs['profile_img'],
        # kwargs['card_id_img'],kwargs['commercial_record_img'],kwargs['country']
        # ,is_company=is_company,  phone_number = phone_number, profile_img = profile_img ,card_id_img = card_id_img ,commercial_record_img = commercial_record_img,country = country
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    is_company = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=32,default=False)
    profile_img = models.CharField(max_length=255,default=False)
    card_id_img =  models.CharField(max_length=255,default=False)
    commercial_record_img = models.CharField(max_length=255,default=False)
    country = models.CharField(max_length=32,default=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }





