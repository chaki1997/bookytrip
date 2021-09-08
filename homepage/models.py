from django.db import models


class FrontVideos(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	video = models.FileField(upload_to='homepage', null=True, blank=True)

	class Meta:
		verbose_name_plural = "Front Videos"


class HomePageDestination(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField()
	video = models.FileField(upload_to='homepage')

    
class HomePageInterestingFacts(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField()
	image = models.ImageField(upload_to='homepage')