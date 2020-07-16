from django.shortcuts import render
from django.utils import timezone
from main.models import todo
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  tasks = todo.objects.all().order_by("-added_date")
  return render(request,'index.html',{'tasks':tasks})

@csrf_exempt
def add_task(request):
  if request.method == "POST":
    task_h = request.POST["task_h"]
    task_d = request.POST["task_d"]
    content_add_time = timezone.now()
    if todo.objects.create(task_h=task_h,task_d=task_d,added_date=content_add_time):
      return HttpResponseRedirect('add_task'),HttpResponse("Task added")
  else:
    return render(request, "add.html")

@csrf_exempt
def del_task(request, num):
  todo.objects.get(id=num).delete()
  return HttpResponseRedirect('/')


