from turtle import title
from home.models import Projects, Tasks
from django.forms import  ModelForm
from django import forms

class CreateProjectForm(ModelForm):
    class Meta:
        model=Projects
        fields='__all__'

class CreateTaskForm(ModelForm):
    class Meta:
        model=Tasks
        fields='__all__'
        exclude=['is_completed']
        