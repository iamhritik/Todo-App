from django.db import models
from django.utils import timezone
# Create your models here.
"""
  todo_tasks -> Model for every individual task
  Main_T -> Relation between Main task and every individual sub_task
"""
class todo_tasks(models.Model): 
  task_owner = models.CharField(max_length=100)
  task_h = models.CharField(max_length=200, unique=True)
  task_d = models.CharField(max_length=400, blank=True, null=True)
  added_date = models.DateTimeField()
  end_date = models.DateTimeField(blank=True,null=True)
  complete = models.BooleanField()
  def __str__(self):
  	return f"{self.task_owner}:{self.task_h}"