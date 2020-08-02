from django.contrib import admin
from django.conf import settings
from main import views
from main.views import chartdata
from django.urls import path

urlpatterns=[
	path('',views.index, name="index"),
	path('taskadd',views.taskadd, name="taskadd"),
	path('taskdelete/<int:taskid>',views.taskdelete, name="taskdelete"),
	path('taskdetail/<int:taskid>',views.taskdetail, name="taskdetail"),
	path('subtaskdelete/<int:subid>/<int:taskid>', views.subtaskdelete),
	path('taskcomplete/<int:taskid>',views.taskcomplete, name="taskcomplete"),
	path('chart',views.chart, name="chart"),
	path('api/chart/data/', chartdata.as_view(), name="api-data"),
	]

