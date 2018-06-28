from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ["name", "description"]
	model = Project

admin.site.register(Project, ProjectModelAdmin)