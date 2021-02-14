from django import forms
import bootstrap_datepicker_plus as datetimepicker

from .models import Task


class TaskForm(forms.ModelForm):
    # deadline = forms.SplitDateTimeField(label='期限(日時)')

    class Meta:
        model = Task
        fields = ("task_name", 'deadline')
        widgets = {
            'deadline': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            )
        }