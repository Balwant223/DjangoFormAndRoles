from django.shortcuts import render
from .forms import ProjectForm
from .models import Project


def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project()
            project.name = form.cleaned_data['name']
            project.start = form.cleaned_data['start']
            project.end = form.cleaned_data['end']
            project.value = form.cleaned_data['value']
            project.save()
    else:
        form = ProjectForm()
    context = {'form': form}
    return render(request, 'MyApp/create.html', context)

def listProject(request):
    projects=Project.objects.all()
    print(projects)
    context={'projects':projects}
    return render(request,'MyApp/list.html',context)
