from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,max_length=254)
    phone_number = PhoneNumberField(max_length=14,help_text='e.g:0912 123 4567',blank=True, null=True)
    is_author = models.BooleanField(_("is author?"), default=False)

