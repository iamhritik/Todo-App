from django.shortcuts import render
from django.utils import timezone
from main.models import todo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  tasks = todo.objects.all().order_by("-added_date")
  return render(request,'index.html',{'tasks':tasks})

@csrf_exempt
def add_task(request):
  content = request.POST["content"]
  content_add_time = timezone.now()
  todo.objects.create(text=content,added_date=content_add_time)
  print(todo.objects.all().count())
  return HttpResponseRedirect('/')

@csrf_exempt
def del_task(request, num):
  todo.objects.get(id=num).delete()
  return HttpResponseRedirect('/')


