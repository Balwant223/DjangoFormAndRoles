from django.urls import path
from . import views
app_name = 'MyApp'

urlpatterns = [
    path('signin/',views.sign_up,name='signup'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('',views.projectHome,name='home'),
    path('edit/<int:pk>/',views.editProject,name='edit'),
    path('delete/<int:pk>/',views.deleteProject, name='delete'),
]
