from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ProjectForm
from .models import Project


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

def deleteProject(request,pk):
    print(pk)
    project=Project.objects.get(id=pk)
    project.delete()
    return HttpResponse('')

