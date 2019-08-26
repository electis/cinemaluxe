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
        context.update({'menu': models.Menu.objects.first()})
        return render(request, 'index.html', context)
        # return HttpResponse(status=403)
