from django.contrib import admin
from django.conf import settings
from main import views
from django.urls import path

app_name = 'main'

urlpatterns=[
	path('',views.home, name='home'),
    path('add_task', views.add_task, name="add_task"),
    path('del_task/<int:num>/', views.del_task),
    path('subtask_del_task/<int:num>/', views.subtask_del_task),
    path('task_detail/<int:num>/', views.detail_tasks, name="detail_tasks"),
	]
