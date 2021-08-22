from django.urls import path
from . import views
app_name = 'MyApp'

urlpatterns = [
    path('',views.projectHome,name='home'),
    path('delete/<int:pk>/',views.deleteProject, name='delete'),
]
