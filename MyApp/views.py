from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProjectForm
from .models import Project


def projectHome(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            print('Hii')
    else:
        form = ProjectForm()

    projects=Project.objects.all()
    context = {'form': form,'projects':projects}
    return render(request,'MyApp/home.html',context)

def deleteProject(request,pk):
    print(pk)
    project=Project.objects.get(id=pk)
    project.delete()
    return HttpResponseRedirect('')

