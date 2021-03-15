from django import forms
from .models import Tasks, TaskList

class TaskListForm(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # in the class replace the parameter with : forms.ModelForm for below to be working 
    # else forms.Form 
    class Meta:
        model = TaskList
        fields = '__all__'
        widgets = {
        'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'  # can have the vlaue as a list those we want to appear in the webpage ('__all__' will automatically consider all the fields.).
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }