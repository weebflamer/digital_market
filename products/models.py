from django.db import models
from django.utils.translation import gettext_lazy as _


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
    title = models.CharField(_("title"),max_length=100)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"),blank=True, upload_to="products")
    is_enable = models.BooleanField(_("is enable"),default=True)
    categories = models.ManyToManyField('Category', verbose_name=_("categories"), blank=True)
    created_at = models.DateTimeField(_("created time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updated time"),auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = _("product")
        verbose_name_plural = _("products")


class File(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    file = models.FileField(_("file"), upload_to="files/%Y/%m/%d")
    title = models.CharField(_("title"),max_length=100)
    is_enable = models.BooleanField(_("is enable"),default=True)
    created_at = models.DateTimeField(_("created time"),auto_now_add=True)
    updated_at = models.DateTimeField(_("updated time"),auto_now=True)


    class Meta:
        db_table = 'file'
        verbose_name = _("file")
        verbose_name_plural = _("files")


