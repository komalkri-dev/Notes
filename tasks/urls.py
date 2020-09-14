from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:Private_key>/', views.updateTask, name='update_task'),
    path('delete/<str:Private_key>/', views.deletTask, name = 'delete'),
]