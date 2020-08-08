from django.contrib import admin
from django.conf import settings
from main import views
from django.urls import path

urlpatterns=[
	path('',views.home, name="home"),
    path('add_task', views.add_task, name="add_task"),
    path('del_task/<int:id>', views.del_task, name="del_task"),
    path('add_sub/<int:num>', views.add_sub, name="add_sub"),
    path('del_sub/<int:num1>/<int:num2>', views.del_sub, name="del_sub"),
    path('complete/<int:taskid>', views.complete, name="complete"),
    path('tasks', views.tasks, name="tasks")
	]
#path('del_sub/<int:num>/<int:id>', views.del_sub, name="del_sub")

