from django.db import models
from django.utils import timezone

#---------MODELS DESCRIPTION--------
#maintask:for your main tasks
#subtask: for subtask
#notes: for add some notes in the task
#taskstatus: to check the task status
#userinfo: to store user information..

class maintask(models.Model):
  task_name=models.CharField(max_length=100,blank=True,null=True)
  createdby = models.ForeingKey(userinfo, on_delete = models.CASCADE, related_name="tasks")
  add_date=models.DateTimeField(auto_now_add=True)
  end_date=models.DateTimeField(null=True)
  def __str__(self):
  	return self.task_name

class subtask(models.Model):
  subtask_name=models.CharField(max_length=30,null=True)
  parenttask=models.ForeignKey(maintask, on_delete=models.CASCADE, related_name="subtasks")
  def __self__(self):
    return self.subtask

class notes(models.Model):
  notes_name=models.CharField(max_length=150,null=True)
  parenttask=models.ForeignKey(maintask, on_delete=models.CASCADE, related_name="notes")
  def __self__(self):
    return self.notes_name

class taskstatus(models.Model):
  options = (
    ('pending','pending'),
    ('completed','completed'),
    ('breached','breached'),
  )
  status=models.CharField(max_length=10,choices=options,default='pending')
  task = models.OneToOneField(maintask, on_delete=models.CASCADE, related_name="status")
  def __self__(self):
    return self.task_status

class userinfo(models.Model):
  username=models.CharField(max_length=100)
  useremail=models.CharField(max_length=100)
  def __self__(self):
    return username









