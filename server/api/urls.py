from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all),
    path('add/', views.post),
    path('adduser/', views.postuser),
    path('addorder/', views.postorder),
    path('allorders/', views.get_all_orders),
    path('notrecived/', views.get_not_recived_order),
    path('getuser/<int:pk>', views.get_user_by_id),
    path('getitem/<int:pk>', views.get_item_by_id),
    path('recive/', views.set_recived),
    path('getuser/', views.get_user_role)
]