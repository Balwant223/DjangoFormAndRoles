from django import forms
from django.forms import fields
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'