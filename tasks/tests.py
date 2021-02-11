from django.test import TestCase

from .models import Task


class TaskModelTests(TestCase):
    def test_progress_rate_with_no_subtask(self):
        """
        progress_rate() returns None for tasks that have no subtask
        """
        nosub_task = Task()
        self.assertIs(nosub_task.progress_rate(), None)
