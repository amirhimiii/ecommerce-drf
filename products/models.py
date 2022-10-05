from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model



class ActiveManager(models.Manager):
    def active_product(self):
        return super().get_queryset().filter(active=True)





User = get_user_model()
class Product(models.Model):
    user = models.ForeignKey(User ,verbose_name=_("user"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    active = models.BooleanField(_("active?"), default=True)

    datetime_created = models.DateTimeField(_("datetime_created"), auto_now_add=True)
    datetime_modified = models.DateTimeField(_("datetime_modified"), auto_now=True)


    objects = ActiveManager()

    def __str__(self):
        return self.title
    


    @property
    def get_username(self):
        return self.user.username