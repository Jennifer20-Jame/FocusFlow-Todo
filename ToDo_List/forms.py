from django import forms
from .models import Task
from datetime import date
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'due_date', 'status']
        widgets = {
            #'title': forms.TextInput(attrs={'placeholder': 'Enter task title'}),
            #'content': forms.Textarea(attrs={'placeholder': 'Enter task details'}),
            'due_date': forms.DateInput(
                attrs={
                    'type': 'date',                  
                    'placeholder': 'Select due date',
                    'min': date.today().isoformat()  
                }
            ),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < date.today():
            raise ValidationError("Due date cannot be in the past.")
        return due_date