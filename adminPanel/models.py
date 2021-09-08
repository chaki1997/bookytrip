from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator


class Country(models.Model):
	country = CountryField()

	class Meta:
		verbose_name_plural = "Country"

	def __str__(self):
		return self.country.name


class City(models.Model):
	highway = models.ForeignKey(Country, on_delete=models.CASCADE)
	city = models.CharField(max_length=128)
	city_video = models.FileField(null=True, blank=True)
	x_c = models.IntegerField(null=True, blank=True)
	y_c = models.IntegerField(null=True, blank=True)


class FooterDescription(models.Model):
	description = models.TextField()
	address = models.CharField(max_length=100)
	email = models.EmailField()
	phoneKA = models.CharField(max_length=100, default='+995 ')
	phoneEN = models.CharField(max_length=100, default='+44 ')
	phoneFR = models.CharField(max_length=100, default='+33 ')
	phoneAZ = models.CharField(max_length=100, default='+994 ')
	phoneDE = models.CharField(max_length=100, default='+49 ')
	phoneES = models.CharField(max_length=100, default='+34 ')
	phoneHY = models.CharField(max_length=100, default='+374 ')
	phoneIT = models.CharField(max_length=100, default='+39 ')
	phoneRU = models.CharField(max_length=100, default='+7 ')

	def __str__(self):
		return self.email


#====================THEMED PACK OPTIONS============================


class ThemedPackReservation(models.Model):
	pack = models.ForeignKey(on_delete=models.CASCADE, to='themedTour.ThemedPack')
	date = models.DateField()
	quantity = models.IntegerField()
	calendar_price = models.DecimalField(max_digits=50, decimal_places=2)

	def __str__(self):
		return str(self.date)


class ThemedPackDuration(models.Model):
	duration = models.IntegerField(validators=[MinValueValidator(5)],unique=True)

	def __str__(self):
		return str(self.duration)


class ThemedPackVariety(models.Model):
	pack_variety = models.CharField(max_length=256)


	def __str__(self):
		return self.pack_variety


class ThemedPackPrice(models.Model):
	connect_pack_price = models.ForeignKey(on_delete=models.CASCADE, to='themedTour.ThemedPack')
	price_start_date = models.DateField()
	price_end_date = models.DateField()
	dynamic_price = models.DecimalField(max_digits=50, decimal_places=2)


class ThemedPackTravelersQuantity(models.Model):
	connect_pack_quantity = models.ForeignKey(on_delete=models.CASCADE, to='themedTour.ThemedPack')
	quantity_start_date = models.DateField()
	quantity_end_date = models.DateField()
	dynamic_quantity = models.IntegerField()


class CarMark(models.Model):
	car_mark = models.CharField(max_length=128)

	def __str__(self):

		return self.car_mark


#====================END THEMED PACK OPTIONS============================



class TermsAndConditions(models.Model):
	text = models.TextField()



class PrivacyPolicy(models.Model):
	text = models.TextField()


class DefaultPriceAdd(models.Model):
	add_price = models.DecimalField(max_digits=50, decimal_places=2)


class SupplierPercentageAdd(models.Model):
	supplier = models.ForeignKey(to='registration.Account', on_delete=models.CASCADE)
	percentage = models.IntegerField()
