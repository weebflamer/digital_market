from django.db import models
from django.utils.translation import pgettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,verbose_name=_('parent'))
    title = models.CharField(_("title"),max_length=100)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"),blank=True, upload_to="categories")
    is_enable = models.BooleanField(_("is enable"),default=True)
    created_at = models.DateTimeField(_("created time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updated time"),auto_now=True)

class Meta :
    db_table = 'category'
    verbose_name = _("category")
    verbose_name_plural = _("categories")


class Product(models.Model):
    pass

class File(models.Model):
    pass

