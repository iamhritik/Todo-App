from django.contrib import admin
from django.conf import settings
from main import views
from django.urls import path

urlpatterns=[
	path('',views.home, name="home"),
	path('signup',views.signup, name="signup"),
    path('add_task', views.add_task, name="add_task"),
    path('del_task/<int:id>', views.del_task, name="del_task"),
    path('complete/<int:taskid>', views.complete, name="complete"),
    path('tasks', views.tasks, name="tasks"),
    path('add_end_date/<int:num>', views.add_end_date, name="add_end_date"),
	]
#path('del_sub/<int:num>/<int:id>', views.del_sub, name="del_sub")

