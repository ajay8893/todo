from django.urls import path
from . import views

urlpatterns = [

    # task views
    path('', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_add'),
    path('edit/<task_id>/', views.task_update, name='task_edit'),
    path('delete/<task_id>/', views.task_delete, name='task_delete'),
    path('complete/<task_id>/', views.task_complete, name='task_complete'),

    # auth views
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
