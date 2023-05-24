from django.shortcuts import render
from django.http import HttpResponse


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
    page = "projects"
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i

    return render(request, 'projects/single-project.html', {'project': projectObj})
