from django.shortcuts import render
from .models import FrontVideos, HomePageDestination, HomePageInterestingFacts
from adminPanel.models import Country, FooterDescription, ThemedPackDuration, City
from components.models import WhyUs

def home_view(request):
	front_videos1 = FrontVideos.objects.get(id=1)
	front_videos2 = FrontVideos.objects.get(id=2)

	cities = City.objects.all()
	countries = Country.objects.all()
	durations = ThemedPackDuration.objects.all().order_by("duration")

	destination = HomePageDestination.objects.get(id=1)

	facts = HomePageInterestingFacts.objects.all()

	why_us = WhyUs.objects.all()
	
	context = {
		'themeVideo':front_videos1,
		'personalVideo':front_videos2,
		'countries':countries,
		'durations': durations,
		'cities':cities,
		'destination':destination,
		'facts':facts,
		'why_us':why_us,
	}
	return render(request,'homepage/homepage.html',context)


