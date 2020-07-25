from django.shortcuts import render
from django.utils import timezone
from main.models import maintasks,subtasks
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail as sm
from datetime import datetime, timedelta

#index view
def index(request):
  task = maintasks.objects.all()
  return render(request,'index.html',{'tasks':task,'time':timezone.now()})

#view to add task 
@csrf_exempt
def taskadd(request):
  if request.method=="POST":#take input from the forms and save it in model
    taskname=request.POST["taskname"]
    taskdetail=request.POST["taskdetail"]
    enddate=request.POST["enddate"]
    submitdate=timezone.now()
    if maintasks.objects.create(task_name=taskname,task_detail=taskdetail,added_date=submitdate,end_date=enddate,complete=False):
      return HttpResponseRedirect('taskadd')
  else:
    return render(request,'add.html')#when you submit nothing

#view to delete task
@csrf_exempt
def taskdelete(request,taskid):
  task=maintasks.objects.get(id=taskid).delete()
  return HttpResponseRedirect('/')


#view to complete a task
@csrf_exempt
def taskcomplete(request,taskid):
  task=maintasks.objects.get(id=taskid)
  task.complete=True
  task.save()
  return HttpResponseRedirect('/')


#view to show a task
@csrf_exempt
def taskdetail(request,taskid):
  task=maintasks.objects.get(id=taskid)
  subname=subtasks.objects.filter(parenttask_id=taskid).order_by('-id')
  if request.method=="POST":
    name=request.POST["subtask"]
    subtasks.objects.create(subtask=name,parenttask=task,subtask_status=False)
    return HttpResponseRedirect('/taskdetail/'+str(taskid))
  else:
    return render(request, 'detail.html',{'task':task, 'subname':subname})


#view to delete subtasks
@csrf_exempt
def subtaskdelete(request,subid,taskid):
    taskname=subtasks.objects.get(id=subid)
    taskname.subtask_status=True
    taskname.save()
    return HttpResponseRedirect('/taskdetail/'+str(taskid))
