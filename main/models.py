from django.db import models
from django.utils import timezone
# Create your models here.

class todo_tasks(models.Model):
  task_h=models.CharField(max_length=200, unique=True, null=True)
  task_d = models.CharField(max_length=400, blank=True, null=True)
  added_date=models.DateTimeField()
  end_date = models.DateTimeField(blank=True)
  complete = models.BooleanField()
  def __str__(self):
  	return f"{self.task_h}"

class Main_t(models.Model):
  main_t = models.ForeignKey(todo_tasks, on_delete=models.CASCADE, related_name="maintask")
  sub_t = models.ManyToManyField(todo_tasks, blank=True, related_name="subtask")

  def main_task(self):
    return f"{self.main_t}"

  def __str__(self):
    return f"{self.main_t}"
