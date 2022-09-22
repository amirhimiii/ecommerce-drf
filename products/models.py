from django.db import models
from django.utils.translation import gettext_lazy as _


class Products(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    active = models.BooleanField(_("active?"), default=True)

    datetime_created = models.DateTimeField(_("datetime_created"), auto_now_add=False)
    datetime_modified = models.DateTimeField(_("datetime_modified"), auto_now=False)
