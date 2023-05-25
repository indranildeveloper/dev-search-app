from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


projectsList = [
    {
        "id": "1",
        "title": "E-commerce Web app",
        "description": "Fully functional e-commerce website"
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "My portfolio website"
    },
    {
        "id": "3",
        "title": "DevConnector",
        "description": "Social Media app for developers"
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})
