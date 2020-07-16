from django.db import models
from django.utils import timezone
# Create your models here.

class todo_tasks(models.Model):
  task_h=models.CharField(max_length=200)
  task_d = models.CharField(max_length=400)
  added_date=models.DateTimeField()

  def __str__(self):
  	return self.task_h
