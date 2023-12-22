from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True, max_length=200)
    username = models.CharField(max_length=200,
                                # validators=[
                                #     RegexValidator(regex=r'\w$', message="Enter vaild value (a-z,0-9,-,_)",code="invalid_registration")]
                                    )
    phone_number = PhoneNumberField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login= models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']
    def __str__(self):
        return self.username
    