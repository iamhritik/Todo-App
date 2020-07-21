# Generated by Django 3.0.8 on 2020-07-21 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_h', models.CharField(max_length=200, null=True, unique=True)),
                ('task_d', models.CharField(blank=True, max_length=400, null=True)),
                ('added_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Main_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintask', to='main.todo_tasks')),
                ('sub_t', models.ManyToManyField(blank=True, related_name='subtask', to='main.todo_tasks')),
            ],
        ),
    ]
