from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254)
    is_author = models.BooleanField(_("is author?"), default=False)