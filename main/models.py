from django.db import models
from django.utils import timezone
# Create your models here.

class maintasks(models.Model):
  task_name=models.CharField(max_length=200,blank=True,null=True)
  task_detail = models.CharField(max_length=400,blank=True,null=True)
  added_date=models.DateTimeField()
  end_date = models.DateTimeField(null=True)
  complete = models.BooleanField()
  emailid = models.CharField(max_length=20,null=True)
  def __str__(self):
  	return self.task_detail

class subtasks(models.Model):
  subtask=models.CharField(max_length=30,null=True)
  parenttask = models.ForeignKey(maintasks, on_delete=models.CASCADE)
  subtask_status=models.BooleanField()
  def __self__(self):
    return self.subtask

