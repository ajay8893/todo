from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('/add/<task_id>/', views.task_create, name='task_add'),
    path('/edit/<task_id>/', views.task_update, name='task_edit'),
    path('/delete/<task_id>/', views.task_delete, name='task_delete'),
    path('/complete/<task_id>/', views.task_complete, name='task_complete'),
]
