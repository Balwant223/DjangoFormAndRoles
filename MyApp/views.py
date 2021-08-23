from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ProjectForm,LogInForm,SignInForm
from .models import Project,User,DeletedProjects
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.forms.models import model_to_dict
from .decorators import is_u_manager
from django.contrib import messages

@login_required
def projectHome(request):
    if request.method == 'POST':
        form=ProjectForm()
        if 'pro_submit' in request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                project=Project()
                project.name=form.cleaned_data['name']
                project.start=form.cleaned_data['start']
                project.end=form.cleaned_data['end']
                project.value=form.cleaned_data['value']
                project.save()
                return HttpResponseRedirect(reverse('MyApp:home'))
    else:
        form = ProjectForm()

    projects=Project.objects.all()
    deleted=DeletedProjects.objects.all()
    #Securing delted data to all viewers 
    if request.user.is_manager:
        context = {'form': form,'projects':projects,'deleted':deleted}
    else:
        context={'form': form,'projects':projects}
    return render(request,'MyApp/home.html',context)

@login_required
@is_u_manager
def editProject(request,pk):
    instance=get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project=Project.objects.get()
            project.name=form.cleaned_data['name']
            project.start=form.cleaned_data['start']
            project.end=form.cleaned_data['end']
            project.value=form.cleaned_data['value']
            project.save()
            return HttpResponseRedirect(reverse('MyApp:home'))
    else:
        form = ProjectForm(initial=model_to_dict(instance))
    context = {'form': form}
    return render(request,'MyApp/edit.html',context)

@login_required
def viewProject(request,pk):
    instance=get_object_or_404(Project, id=pk)
    form = ProjectForm(initial=model_to_dict(instance))
    context = {'form': form}
    return render(request,'MyApp/details.html',context)


def userLogin(request):
    if request.method=='POST':
        form=LogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('MyApp:home'))
            else:
                messages.error(request,'Username or Password not correct')
                return HttpResponseRedirect(reverse('MyApp:login'))
    else:
        form=LogInForm()
    context={'form':form}
    return render(request,'MyApp/login.html',context)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('MyApp:login'))

def sign_up(request):
    if request.method=='POST':
        form=SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd['username']).exists():
                messages.error(request,'Username Already Exists')
                return HttpResponseRedirect(reverse('MyApp:signup'))
                
            else:
                user=User()
                user.username=cd['username']
                user.set_password(cd['password'])
                user.is_manager=cd['is_manager']
                user.save()
                return HttpResponseRedirect(reverse('MyApp:login'))
    else:
        form=SignInForm()
    context={'form':form}
    return render(request,'MyApp/signup.html',context)

@login_required
@is_u_manager
def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    deletedpro=DeletedProjects.objects.create(name=project.name,start=project.start,end=project.end,value=project.value)
    deletedpro.save()
    project.delete()
    return HttpResponse('')

