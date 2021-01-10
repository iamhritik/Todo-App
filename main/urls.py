from main import views
from django.urls import path


urlpatterns=[
	path('',views.home, name="home"),
	path('signup',views.signup, name="signup"),
    path('del_task/<int:id>', views.del_task, name="del_task"),
    path('complete/<int:taskid>', views.complete, name="complete"),
    path('task-list/<str:pk>', views.task_list, name='task-list'),
    path('task-add/', views.task_add, name='task-add'),
    path('task-update/<str:id>', views.task_update, name='task-update'),
    path('task-delete/<str:id>', views.task_delete, name='task-delete'),
	]
