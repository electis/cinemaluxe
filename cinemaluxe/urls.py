from django.contrib import admin
from django.urls import path, re_path

from cinemaluxe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', views.MainView.as_view()),
]