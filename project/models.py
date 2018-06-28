from django.db import models
from django.urls import reverse

# Create your models here.

def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s" %(instance.id, filename)

class Project(models.Model):
	name = models.CharField(max_length = 120)
	description = models.TextField()
	video = models.CharField(max_length = 1000)
	#image = models.ImageField(upload_to = upload_location, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("project:detail", kwargs={"id":self.id})