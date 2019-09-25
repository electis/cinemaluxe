from django.contrib import admin
from django.urls import path, re_path

from cinemaluxe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/<int:pk>', views.GroupView.as_view()),
    path('groups/', views.GroupsView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('product/<int:pk>', views.ProductView.as_view()),
    re_path(r'^', views.MainView.as_view()),
]
