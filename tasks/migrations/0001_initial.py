# Generated by Django 3.1.6 on 2021-02-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask_name', models.CharField(max_length=50, verbose_name='サブタスク名')),
                ('deadline', models.DateTimeField(verbose_name='期限')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50, verbose_name='タスク名')),
                ('deadline', models.DateTimeField(verbose_name='期限')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
