from django.db import models
from django.utils import timezone
# Create your models here.

class todo_tasks(models.Model):
  task_h=models.CharField(max_length=60)
  task_d = models.CharField(max_length=300)
  added_date=models.DateTimeField()
  def __str__(self):
  	return self.task_h

class subtasks(models.Model):
	taskname=models.CharField(max_length=100)
	maintask=models.ForeignKey(todo_tasks, on_delete=models.CASCADE)
	def __str__(self):
		return self.taskname

class completed_tasks(models.Model):
	task_ch=models.CharField(max_length=60)
	task_cd=models.CharField(max_length=300)
	def __str__(self):
		return self.task_ch