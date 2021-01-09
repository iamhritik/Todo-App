from .models import todo_tasks
from rest_framework import serializers

class TodoTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo_tasks
        fields = ['id','task_h','task_d','added_date','end_date','complete']

