from django.db import models
from django.urls import reverse, reverse_lazy

class Menu(models.Model):
    title = models.CharField(max_length=100)
    title_slug = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='table_item')
    menu_name = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True, related_name='table_name')
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title



class Items(Menu):

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        n = self
        url = ''
        while n:
            url = f'/{n.title_slug}' + url
            n = n.parent
        self.url = url.replace('/', '', 1)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)



    class Meta:
        proxy = True


