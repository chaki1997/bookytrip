from django.db import models
from adminPanel.models import Country
from registration.models import Account
from django.core.validators import MinValueValidator


class ThemedPack(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
	pack_name = models.CharField(max_length=200)
	description = models.TextField()
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
	price = models.DecimalField(max_digits=50, decimal_places=2)
	picture1 = models.ImageField(upload_to='images/themedpack', default='images/brand-2.jpg')
	picture2 = models.ImageField(upload_to='images/themedpack', default='images/brand-2.jpg')
	small_video = models.FileField(upload_to="themedvideos")
	big_video = models.FileField(upload_to="themedvideos")
	trip_variety = models.ForeignKey(to='adminPanel.ThemedPackVariety', null=True, blank=True, on_delete=models.SET_NULL)
	NUMBER_OF_TRAVEL_CHOICES = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
		)
	number_of_travelers = models.CharField(max_length=100, choices = NUMBER_OF_TRAVEL_CHOICES)
	number_of_days = models.ForeignKey(to="adminPanel.ThemedPackDuration", on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	permission = models.BooleanField(default=False)
	notification = models.BooleanField(default=False)

	class Meta:
		verbose_name_plural = "Themed Pack"

	def __str__(self):
		return self.pack_name


class ThemedDaysDescription(models.Model):
	pack_connect_day = models.ForeignKey(ThemedPack, on_delete=models.CASCADE)
	description = models.TextField()

	def __str__(self):
		return self.pack_connect_day.pack_name


class ThemedPackReview(models.Model):
	pack = models.ForeignKey(ThemedPack, on_delete=models.CASCADE)
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	comment = models.TextField()
	stars = models.SmallIntegerField(default=5)
	permition = models.BooleanField(default=False)
	notification = models.BooleanField(default=False)

	def __str__(self):
		return self.user.email

	class Meta:
		verbose_name_plural = "Themed Pack Reviews"


class OrderedThemedPack(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	pack = models.ForeignKey(ThemedPack, on_delete=models.CASCADE)
	order_start_date = models.DateField()
	order_end_date = models.DateField()
	order_travelers = models.PositiveIntegerField(validators=[MinValueValidator(1)])

	def __str__(self):
		return self.pack.pack_name


