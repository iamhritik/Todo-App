from main import views
from django.urls import path


urlpatterns=[
	path('',views.home, name="home"),
	path('signup',views.signup, name="signup"),
    path('del_task/<int:id>', views.del_task, name="del_task"),
    path('complete/<int:taskid>', views.complete, name="complete"),
    path('all-tasks/', views.taskAll, name='all-tasks'),
    path('task-add/', views.task_add, name='task-add'),
    path('edit-task/<str:id>', views.task_update, name='edit-task'),
	]
