from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

# Create your views here.

def home(request): #list items
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

def projects(request):
	queryset_list = Project.objects.all()
	context = {
		"object_list":queryset_list,
	}
	return render(request, "project.html", context)

def test(request):
	return render(request, "test.html")
	
def detail(request, project_id):
	instance = get_object_or_404(Project, id=project_id)
	context = {
		"instance" : instance,
	}
	return render(request, "detail.html", context)