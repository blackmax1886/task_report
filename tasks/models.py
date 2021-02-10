from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    deadline = models.DateTimeField()

    # pro_rate = models.IntegerField(verbose_name='progress rate')

    def __str__(self):
        return self.task_name


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_name = models.CharField(max_length=50)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.subtask_name
