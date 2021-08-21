from django.urls import path
from . import views
app_name = 'MyApp'

urlpatterns = [
    path('',views.projectHome,name='home'),
    path('create/', views.createProject, name='create'),
    path('list/',views.listProject,name='list'),
]
