from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey, CASCADE


class Task(models.Model):
    task_name = models.CharField("タスク名", max_length=50)
    deadline = models.DateTimeField("期限")
    status = models.BooleanField(default=False)
    create_user = ForeignKey(get_user_model(), on_delete=CASCADE)

    def __str__(self):
        return self.task_name

    def progress_rate(self):
        from math import floor
        subtasks_num = self.subtask_set.count()
        if subtasks_num != 0:
            complete_num = self.subtask_set.filter(status=True).count()
            return floor((complete_num / subtasks_num) * 100)


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_name = models.CharField("サブタスク名", max_length=50)
    deadline = models.DateTimeField("期限")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subtask_name
