import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Task


def create_task(task_name="", days=0, status=False):
    """
    Create a task with the given 'task_name' and published the given number of 'days'
    offset to now (negative for tasks over deadline)
    :param task_name: content of task
    :param days: the number of days offset to now, indicating deadline
    :param status: Boolean. if task was completed, True.
    :return:Boolean
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Task.objects.create(task_name=task_name, deadline=time, status=status)


class TaskModelTests(TestCase):
    def test_progress_rate_with_no_subtask(self):
        """
        progress_rate() returns None for tasks that have no subtask
        """
        nosub_task = Task()
        self.assertIs(nosub_task.progress_rate(), None)


class TaskIndexViewTests(TestCase):
    def test_no_tasks(self):
        """
        if no tasks exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Have a break time!")
        self.assertQuerysetEqual(response.context['closest_task_list'], [])

    def test_completed_tasks(self):
        """
        Tasks with status: True (completed) are NOT displayed on the index page.
        """
        create_task(status=True)
        response = self.client.get(reverse('tasks:index'))
        self.assertContains(response, "Have a break time!")
        self.assertQuerysetEqual(response.context['closest_task_list'], [])

    def test_completed_task_and_uncompleted_task(self):
        """
        tasks with status: both True and False, only tasks with status: False are displayed.
        """
        create_task(task_name="completed task", status=True)
        create_task(task_name="uncompleted task", status=False)
        response = self.client.get(reverse('tasks:index'))
        self.assertQuerysetEqual(response.context['closest_task_list'], ['<Task: uncompleted task>'])

    def test_two_uncompleted_task(self):
        """
        The tasks index page may display multiple tasks.
        """
        create_task(task_name="uncompleted task 1", days=1, status=False)
        create_task(task_name="uncompleted task 2", days=2, status=False)
        response = self.client.get(reverse('tasks:index'))
        self.assertQuerysetEqual(response.context['closest_task_list'],
                                 ['<Task: uncompleted task 1>', '<Task: uncompleted task 2>'])
