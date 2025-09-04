from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('task-list/', views.task_list, name='task-list'),
    path('task/<int:pk>/', views.task_detail, name='view-task'),
    path('task/<int:pk>/done/', views.task_done, name='task-done'),
    path('add_task/', views.add_task, name='add-task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete-task'),
]