from django.shortcuts import render
from django.utils import timezone
import json
from django.core import serializers
from main.models import todo_tasks, Main_t
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail as sm
from datetime import datetime, timedelta

# Create your views here.
"""
  Views :
    home -> Main Landing Page view
    add_task -> Adding Main Task
    add_sub -> Adding Sub task
    del_task -> For deleting Main task and every sub task it contains
    del_sub -> Deleting Sub tasks from main task
    complete -> for represting complete functionality for sub tasks and main task
"""
def home(request):
  tasks = Main_t.objects.all() #collecting all main Tasks
  return render(request,'sample1.html',{
    "tasks" : tasks
  })

def tasks(request):
  maint = Main_t.objects.all()
  tasks = [{"main_id":i.id,"tasks":{"id":i.main_t.id,"task_h":i.main_t.task_h,"complete":i.main_t.complete}} for i in Main_t.objects.all()]
  jtasks = json.dumps(tasks)
  return HttpResponse(f'{jtasks}')


@csrf_exempt
def add_task(request):
  if request.method == "POST":
    task_h = request.POST["task_h"]
    task_d = request.POST["task_d"]
    content_add_time = timezone.now()
    #end_date = request.POST["task_end_date"]
    task = todo_tasks.objects.create(task_h=task_h,task_d=task_d,added_date=content_add_time,complete=False)
    a = Main_t.objects.create(main_t=task)
    #resp = json.dumps({"id":a.id})
    return JsonResponse({"id":a.id,"task_id":a.main_t.id})

@csrf_exempt
def add_sub(request, num):
  if request.method == "POST":
    try :
      task = todo_tasks.objects.get(task_h=request.POST["subtask"])
      maint = Main_t.objects.get(id=num)
      maint.sub_t.add(task)
    except todo_tasks.DoesNotExist:
      task = todo_tasks.objects.create(task_h=request.POST["subtask"],added_date=timezone.now(),complete=False)
      maint = Main_t.objects.get(id=num)
      maint.sub_t.add(task)
    return HttpResponseRedirect(reverse('home'))


@csrf_exempt
def del_task(request, id):
  main_task = Main_t.objects.get(id=id)
  main_task.sub_t.all().delete()
  main_task.save()
  todo_tasks.objects.get(task_h=main_task).delete()
  return HttpResponse(b'Successful')

@csrf_exempt
def del_sub(request, num1, num2):
  maint = Main_t.objects.get(id=num1)
  maint.sub_t.get(id=num2).delete()
  maint.save()
  return HttpResponseRedirect(reverse('home'))

@csrf_exempt
def complete(request, taskid):
  if request.method == "POST":
    task = todo_tasks.objects.get(id=taskid)
    try:
      maint = Main_t.objects.get(main_t=task)
      maint.main_t.complete = True
      maint.main_t.save()
      maint.save()
      return HttpResponse(b'Done')
    except :
      return HttpResponse(b'Not Done')
    """maint = Main_t.objects.get(id=mainid)
    subt = maint.sub_t.get(id=subid)
    if request.POST["complete_var"] == "True":
      subt.complete = True
      subt.save()
      if maint.sub_t.filter(complete=False).count() == 0:
        sm(subject = 'Task Completed !!! ',message = maint.main_t.task_h,from_email = 'ToDo-App <shahiblogs@gmail.com>',recipient_list = ['hritik.99@outlook.com','cocdrive89@gmail.com',],fail_silently=False,)
        maint.main_t.complete = True
        maint.main_t.save()
        sendmail(mainid)
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home')) 
    """

def sendmail(mainid):
  maint=Main_t.objects.get(id=mainid)
  sm(subject = 'Task Completed !!! ',message = maint.main_t.task_d,from_email = 'ToDo-App <example@gmail.com>',recipient_list = ['example@outlook.com',],fail_silently=False,)

