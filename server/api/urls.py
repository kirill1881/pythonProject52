from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all),
    path('add/', views.post),
    path('adduser/', views.post),
    path('addorder/', views.postorder),
    path('notrecived/', views.get_not_recived_order)
]