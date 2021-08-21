from django.urls import path
from .views import createProject

app_name = 'MyApp'

urlpatterns = [
    path('create', createProject, name='create'),
]
