from django.contrib import admin
from django.apps import apps
from cinemaluxe import models
from singlemodeladmin import SingleModelAdmin

@admin.register(models.Menu)
class MenuAdmin(SingleModelAdmin):
   readonly_fields = ('pk',)


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
   readonly_fields = ('pk',)


model_list = apps.get_models()

for model in model_list:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
