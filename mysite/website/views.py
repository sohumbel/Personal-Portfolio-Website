from django.shortcuts import render
from website.models import Project, Work
# Create your views here.
def cover(request):
    return render(request, "index.html",{})
def project_index(request):
    projects = Project.objects.all()
    url = str(Project.image).replace("static",'')
    context = {
        'projects' : projects, 'url' : url
    }
    return render (request, "project_index.html", context)