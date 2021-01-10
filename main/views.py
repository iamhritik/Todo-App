from django.shortcuts import render
from django.utils import timezone
import json
from main.models import todo_tasks
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail as sm
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoTaskSerializer

# Create your views here.
"""
  Views :
    home -> Main Landing Page view
    add_task -> Adding Main Task
    add_sub -> Adding Sub task
    del_task -> For deleting Main task and every sub task it contains
    del_sub -> Deleting Sub tasks from main task
    complete -> for represting complete functionality for sub tasks and main task


    tasks = Main_t.objects.all() #collecting all main Tasks
      return render(request,'sample1.html',{
    "tasks" : tasks
  })

"""

@login_required(login_url='/signup')
def home(request):
  owner = request.user
  return render(request,'sample1.html' , {'sample_task_owner':owner})

def signup(request):
  return render(request, 'signup.html', {})

@csrf_exempt
def del_task(request, id):
  main_task = todo_tasks.objects.get(id=id)
  main_task.delete()
  return HttpResponse(b'Successful')

@csrf_exempt
def complete(request, taskid):
  if request.method == "POST":
    try:
      task = todo_tasks.objects.get(id=taskid)
      task.complete = True
      task.save()
      return HttpResponse(b'Done')
    except :
      return HttpResponse(b'Not Done')

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'All' : '/task-list/',
    'Create': '/task-add/',
    'Update': '/task-update/<str:id>/',
    'Delete': '/task-delete/<str:id>/',
  }

  return Response(api_urls)

@api_view(['GET'])
def task_list(request,pk):
  tasks = todo_tasks.objects.filter(task_owner=pk)
  serializer = TodoTaskSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def task_add(request):
  owner = request.user
  task_h = request.data['task_h']
  end_date = request.data['end_date'] if request.data['end_date']!= "" else None
  add_time = timezone.now()
  complete = False
  task = todo_tasks.objects.create(task_owner=owner,task_h=task_h,end_date=end_date,added_date=add_time,complete=complete)
  serializer = TodoTaskSerializer(task, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def task_update(request, id):
  task = todo_tasks.objects.get(id=id)
  serializer = TodoTaskSerializer(instance=task,data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request,pk):
  task = todo_tasks.objects.get(id=pk)
  task.delete()

  return Response("Item successfully deleted")
