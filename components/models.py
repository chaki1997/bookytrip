from django.db import models
from registration.models import Account

class Faq(models.Model):
	# Remove on user null and blank
	user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
	question = models.TextField()
	QUESTION_TYPES = (
		('1', 'Pre-Sale Questions'),
		('2', 'Other Type Questions'),
	)
	question_type = models.CharField(max_length=256, choices=QUESTION_TYPES, default='1')
	answer = models.TextField(blank=True,null=True)
	permition = models.BooleanField(default=False)
	notification = models.BooleanField(default=False)


class Contact(models.Model):
	name = models.CharField(max_length=128)
	surname = models.CharField(max_length=128)
	email = models.EmailField()
	text = models.TextField()
	send_time = models.DateTimeField(auto_now=True)
	notification = models.BooleanField(default=False)


class WhyUs(models.Model):
	image = models.ImageField()
	title = models.CharField(max_length=127)
	text = models.TextField()


class About(models.Model):
	cover_file = models.FileField(null=True, blank=True)
	title      = models.CharField(max_length=127)
	image1     = models.ImageField()
	text1      = models.TextField(default="")
	image2     = models.ImageField()
	text2      = models.TextField(default="")
	image3     = models.ImageField()
	text3      = models.TextField(default="")


class Vendor(models.Model):
	logo = models.ImageField()
