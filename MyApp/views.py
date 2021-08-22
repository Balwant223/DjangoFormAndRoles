from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ProjectForm,LogInForm,SignInForm
from .models import Project,User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.forms.models import model_to_dict

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
    context = {'form': form,'projects':projects}
    return render(request,'MyApp/home.html',context)

@login_required
def editProject(request,pk):
    instance=get_object_or_404(Project, id=pk)
    print(model_to_dict(instance))
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
            user=User()
            user.username=cd['username']
            user.set_password(cd['password'])
            user.is_manager=cd['is_manager']
            user.save()
            return HttpResponseRedirect(reverse('MyApp:home'))
    else:
        form=SignInForm()
    context={'form':form}
    return render(request,'MyApp/signup.html',context)

def deleteProject(request,pk):
    print(pk)
    project=Project.objects.get(id=pk)
    project.delete()
    return HttpResponse('')

