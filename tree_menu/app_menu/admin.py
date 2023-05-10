from django.contrib import admin
from app_menu.models import Menu, Items
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q, QuerySet
from .forms import ItemForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'title_slug': ('title',)}
    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]
    fields = ["title", "title_slug"]
    exclude = ['url']

    def get_queryset(self, request: WSGIRequest) -> QuerySet:
        return super().get_queryset(request).filter(Q(parent=None))


@admin.register(Items)
class MenuItemAdmin(admin.ModelAdmin):
    form = ItemForm
    prepopulated_fields = {'title_slug': ('title',)}
    list_display = ["title", "url"]
    list_filter = ["parent"]
    search_fields = ["title"]
    exclude = ['url']
    ordering = ['url']

    def get_queryset(self, request: WSGIRequest) -> QuerySet:
        return super().get_queryset(request).filter(~Q(parent=None))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'menu_name':
            kwargs["queryset"] = Menu.objects.filter(parent=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

