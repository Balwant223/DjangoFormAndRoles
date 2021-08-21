from django.urls import path
from .views import createProject

app_name = 'MyApp'

url_patterns = [
    path('Create', createProject, name='create'),
]
