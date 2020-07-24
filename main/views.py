from django.shortcuts import render
from django.utils import timezone
from main.models import todo_tasks, Main_t
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail as sm
from datetime import datetime, timedelta

# Create your views here.
def home(request):
  tasks = Main_t.objects.all()
  return render(request,'index.html',{'tasks': tasks, 'time' : timezone.now()})

@csrf_exempt
def add_task(request):
  if request.method == "POST":
    task_h = request.POST["task_h"]
    task_d = request.POST["task_d"]
    content_add_time = timezone.now()
    end_date = request.POST["task_end_date"]
    task1 = todo_tasks.objects.create(task_h=task_h,task_d=task_d,added_date=content_add_time,end_date=end_date,complete=False)
    Main_t.objects.create(main_t=task1)
    return HttpResponseRedirect('add_task')
  else:
    return render(request, 'add.html')

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
    return HttpResponseRedirect(reverse("home"))


@csrf_exempt
def del_task(request, id):
  main_task = Main_t.objects.get(id=id)
  main_task.sub_t.all().delete()
  main_task.save()
  todo_tasks.objects.get(task_h=main_task).delete()
  return HttpResponseRedirect(reverse("home"))

@csrf_exempt
def del_sub(request, num1, num2):
  maint = Main_t.objects.get(id=num1)
  maint.sub_t.get(id=num2).delete()
  maint.save()
  return HttpResponseRedirect(reverse("home"))

@csrf_exempt
def complete(request, mainid, subid):
  if request.method == "POST":
    maint = Main_t.objects.get(id=mainid)
    subt = maint.sub_t.get(id=subid)
    if request.POST["complete_var"] == "True":
      subt.complete = True
      subt.save()
      if maint.sub_t.filter(complete=False).count() == 0:
        sm(subject = 'Task Completed !!! ',message = maint.main_t.task_d,from_email = 'ToDo-App <shahiblogs@gmail.com>',recipient_list = ['hritik.99@outlook.com','cocdrive89@gmail.com',],fail_silently=False,)
        maint.main_t.complete = True
        maint.main_t.save()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))

      
    
    

