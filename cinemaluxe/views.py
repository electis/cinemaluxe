from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from cinemaluxe import models


class MainView(View):

    def get(self, request):
        host = request.get_host()
        path_list = [p for p in request.path.split('/') if p]
        print(host, path_list, request.META.get('HTTP_USER_AGENT'), request.META.get('REMOTE_ADDR'), sep=' ~ ')
        context = {}
        context['site'] = models.Site.objects.first()
        context['menu'] = models.MenuItem.objects.all()
        context['banner'] = models.BannerItem.objects.all()
        context['description'] = models.Description.objects.first()
        context['group'] = models.Group.objects.first()
        context['group_list'] = models.GroupItem.objects.all()
        context['gallery'] = models.Gallery.objects.first()
        context['gallery_list'] = models.GalleryItem.objects.all()

        return render(request, 'index.html', context)
        # return HttpResponse(status=403)


class GroupsView(View):

    def get(self, request):
        host = request.get_host()
        path_list = [p for p in request.path.split('/') if p]
        print(host, path_list, request.META.get('HTTP_USER_AGENT'), request.META.get('REMOTE_ADDR'), sep=' ~ ')
        context = {}
        context['site'] = models.Site.objects.first()
        context['menu'] = models.MenuItem.objects.all()
        context['group'] = models.Group.objects.first()
        context['group_list'] = models.GroupItem.objects.all()
        return render(request, 'groups.html', context)
        # return HttpResponse(status=403)


class GroupView(View):

    def get(self, request, pk):
        host = request.get_host()
        path_list = [p for p in request.path.split('/') if p]
        print(host, path_list, request.META.get('HTTP_USER_AGENT'), request.META.get('REMOTE_ADDR'), sep=' ~ ')
        context = {}
        context['site'] = models.Site.objects.first()
        context['menu'] = models.MenuItem.objects.all()
        context['group_item'] = models.GroupItem.objects.get(pk=pk)
        context['product_list'] = models.ProductItem.objects.filter(group__pk=pk)
        return render(request, 'group.html', context)


class ProductView(View):

    def get(self, request, pk):
        host = request.get_host()
        path_list = [p for p in request.path.split('/') if p]
        print(host, path_list, request.META.get('HTTP_USER_AGENT'), request.META.get('REMOTE_ADDR'), sep=' ~ ')
        context = {}
        context['site'] = models.Site.objects.first()
        context['menu'] = models.MenuItem.objects.all()
        context['product'] = models.ProductItem.objects.get(pk=pk)
        return render(request, 'product.html', context)


class ContactView(View):

    def get(self, request):
        host = request.get_host()
        path_list = [p for p in request.path.split('/') if p]
        print(host, path_list, request.META.get('HTTP_USER_AGENT'), request.META.get('REMOTE_ADDR'), sep=' ~ ')
        context = {}
        context['site'] = models.Site.objects.first()
        context['menu'] = models.MenuItem.objects.all()

        return render(request, 'contact.html', context)
