from django.contrib import admin
from django.apps import apps
from cinemaluxe import models
from singlemodeladmin import SingleModelAdmin
from django.utils.html import format_html
from django.urls import reverse, re_path
from django.http import HttpResponseRedirect


@admin.register(models.Site)
class MenuLogoAdmin(SingleModelAdmin):
    pass


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'menu_actions',)

    def order_plus(self, request, pk, *args, **kwargs):
        obj = models.MenuItem.objects.get(pk=pk)
        obj.order += 1
        obj.save()
        return HttpResponseRedirect('/admin/cinemaluxe/menuitem/')

    def order_minus(self, request, pk, *args, **kwargs):
        obj = models.MenuItem.objects.get(pk=pk)
        if obj.order > 1:
            obj.order -= 1
            obj.save()
        return HttpResponseRedirect('/admin/cinemaluxe/menuitem/')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(r'^(?P<pk>.+)/plus/$',  self.admin_site.admin_view(self.order_plus),  name='order-plus',),
            re_path(r'^(?P<pk>.+)/minus/$', self.admin_site.admin_view(self.order_minus), name='order-minus',),
        ]
        return custom_urls + urls

    def menu_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">&minus;</a>&nbsp;'
            '<a class="button" href="{}">&plus;</a>',
            reverse('admin:order-minus', args=[obj.pk]),
            reverse('admin:order-plus', args=[obj.pk]),
        )

    menu_actions.short_description = 'Изменить порядок'
    menu_actions.allow_tags = True


@admin.register(models.BannerItem)
class BannerItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'menu_actions',)

    def order_plus(self, request, pk, *args, **kwargs):
        obj = models.BannerItem.objects.get(pk=pk)
        obj.order += 1
        obj.save()
        return HttpResponseRedirect('/admin/cinemaluxe/banneritem/')

    def order_minus(self, request, pk, *args, **kwargs):
        obj = models.BannerItem.objects.get(pk=pk)
        if obj.order > 1:
            obj.order -= 1
            obj.save()
        return HttpResponseRedirect('/admin/cinemaluxe/banneritem/')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            re_path(r'^(?P<pk>.+)/plus/$',  self.admin_site.admin_view(self.order_plus),  name='order-plus',),
            re_path(r'^(?P<pk>.+)/minus/$', self.admin_site.admin_view(self.order_minus), name='order-minus',),
        ]
        return custom_urls + urls

    def menu_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">&minus;</a>&nbsp;'
            '<a class="button" href="{}">&plus;</a>',
            reverse('admin:order-minus', args=[obj.pk]),
            reverse('admin:order-plus', args=[obj.pk]),
        )

    menu_actions.short_description = 'Изменить порядок'
    menu_actions.allow_tags = True


@admin.register(models.Description)
class DescriptionAdmin(SingleModelAdmin):
    pass


model_list = apps.get_models()

for model in model_list:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
