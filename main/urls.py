from django.contrib import admin
from django.conf import settings
from main import views
from django.urls import path

urlpatterns=[
		path('',views.home, name='home'),
    path('add_task', views.add_task),
    path('del_task/<int:num>/', views.del_task),

	]
