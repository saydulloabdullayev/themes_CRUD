# themes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.theme_list, name='theme_list'),
    path('create/', views.theme_create, name='theme_create'),
    path('<int:pk>/', views.theme_detail, name='theme_detail'),
    path('<int:pk>/update/', views.theme_update, name='theme_update'),
    path('<int:pk>/delete/', views.theme_delete, name='theme_delete'),
]
