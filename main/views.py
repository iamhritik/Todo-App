from django.shortcuts import render
from django.utils import timezone
from main.models import todo_tasks, subtasks
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  tasks = todo_tasks.objects.filter(task_type="True").order_by("-added_date")
  completed=todo_tasks.objects.filter(task_type="False").order_by("-added_date")
  return render(request,'index.html',{'tasks':tasks, 'completed':completed})

@csrf_exempt
def add_task(request):
  if request.method == "POST":
    task_h = request.POST["task_h"]
    task_d = request.POST["task_d"]
    content_add_time = timezone.now()
    if todo_tasks.objects.create(task_h=task_h,task_d=task_d,added_date=content_add_time,task_type=True):
      return HttpResponseRedirect('add_task')
  else:
    return render(request, "add.html")

@csrf_exempt
def compl_task(request, num):
  taskc=todo_tasks.objects.get(id=num)
  taskc.task_type=False
  taskc.save()
  return HttpResponseRedirect('/')

@csrf_exempt
def del_task(request, num):
  mainone=todo_tasks.objects.get(id=num)
  mainone.delete()
  return HttpResponseRedirect('/')

@csrf_exempt
def subtask_del_task(request, num, mum):
  subo=subtasks.objects.get(id=num)
  subo.subtask_type=False
  subo.save()
  a=str(mum)
  return HttpResponseRedirect('/task_detail/'+a)

@csrf_exempt
def detail_tasks(request, num):
  tasks=todo_tasks.objects.get(id=num)
  subtask=subtasks.objects.filter(maintask_id=num, subtask_type="True").order_by('-id')
  totalsubtasks=subtasks.objects.filter(maintask_id=num).count()
  subtaskc=subtasks.objects.filter(maintask_id=num, subtask_type="False")
  if(totalsubtasks==subtaskc.count() and totalsubtasks>0):
    changer=todo_tasks.objects.get(id=num)
    changer.task_type=False
    changer.save()
    return HttpResponseRedirect('/')
  else:
    if request.method == "POST":
      subname=request.POST["subtaskname"]
      if subtasks.objects.create(taskname=subname,maintask=tasks,subtask_type=True):
        return HttpResponseRedirect('/task_detail/'+str(num))
    else:
      return render(request,'detail.html',{'tasks':tasks, 'subtask':subtask, 'subtaskc':subtaskc})
  




