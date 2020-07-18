from django.shortcuts import render
from django.utils import timezone
from main.models import todo_tasks, subtasks
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  tasks = todo_tasks.objects.all().order_by("-added_date")
  return render(request,'index.html',{'tasks':tasks})

@csrf_exempt
def add_task(request):
  if request.method == "POST":
    task_h = request.POST["task_h"]
    task_d = request.POST["task_d"]
    content_add_time = timezone.now()
    if todo_tasks.objects.create(task_h=task_h,task_d=task_d,added_date=content_add_time):
      return HttpResponseRedirect('add_task')
  else:
    return render(request, "add.html")

@csrf_exempt
def del_task(request, num):
  todo_tasks.objects.get(id=num).delete()
  return HttpResponseRedirect('/')

@csrf_exempt
def subtask_del_task(request, num):
  subtasks.objects.get(id=num).delete()
  return HttpResponseRedirect('/')

@csrf_exempt
def detail_tasks(request, num):
  tasks=todo_tasks.objects.get(id=num)
  subtask=subtasks.objects.filter(maintask_id=num)
  subs = subtask.order_by('-id')
  if request.method == "POST":
    subname=request.POST["subtaskname"]
    if subtasks.objects.create(taskname=subname,maintask=tasks):
      return render(request,'detail.html',{'tasks':tasks, 'subs':subs})
  else:
    return render(request,'detail.html',{'tasks':tasks, 'subs':subs})
  


