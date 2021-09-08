from django.shortcuts import render, redirect
from adminPanel.models import Country, FooterDescription, ThemedPackVariety
from .models import ThemedPack, ThemedDaysDescription, ThemedPackReview, OrderedThemedPack
from .forms import ThemedReviewForm, OrderedThemedPackForm
from datetime import timedelta, date, datetime
from adminPanel.models import ThemedPackReservation, City, ThemedPackDuration, DefaultPriceAdd
from django.template.defaulttags import register
from django.contrib import messages
from django.core.exceptions import ValidationError

# ============== for for range loop============
@register.filter
def get_range(value):
    return range(value)
# ===============================================


def themed_tour(request):
	default_price = DefaultPriceAdd.objects.get(id=1)
	country = Country.objects.all()
	themed_pack = ThemedPack.objects.all()
	trip_pack_varieties = ThemedPackVariety.objects.all()
	cities = City.objects.all()
	durations = ThemedPackDuration.objects.all().order_by("duration")
	themed_pack_dict = {}
	for i in themed_pack:
		themed_pack_dict[i]=round((float(i.price)+float(default_price.add_price))/4.07, 2)
	
	context = {
		'countries': country,
		'themedpack': themed_pack,
		'varieties' : trip_pack_varieties,
		'cities':cities,
		'durations':durations,
		'default_price':default_price,
		'themed_pack_dict':themed_pack_dict,
	}
	return render(request, 'themedTour/archive_themed.html', context)


def themed_single(request, id):
	themed_pack = ThemedPack.objects.get(id=id)
	footer = FooterDescription.objects.get(id=1)
	days = ThemedDaysDescription.objects.filter(pack_connect_day=id)
	reviews = ThemedPackReview.objects.filter(pack_id=id)
	# current_time=date.today()
	# if request.user.is_authenticated:
	# 	ordered_packs = OrderedThemedPack.objects.filter(user=request.user)	
	# else:
	# 	ordered_packs = OrderedThemedPack.objects.all()	
	context = {
		'pack': themed_pack,
		'footer': footer,
		'days': days,
		'reviews': reviews,
		# 'ordered_packs':ordered_packs,
		# 'current_time':current_time,

	}

	return render(request, "themedTour/pack_single.html", context)

def thankyou(request):
	
	return render(request, "themedTour/thankyoupage.html")


def themed_review(request, id):
	if request.user.is_authenticated:
		tour = ThemedPack.objects.get(id=id)
		if request.method == 'POST':
			form = ThemedReviewForm(request.POST or None)
			if form.is_valid():
				data = form.save(commit=False)
				data.comment = form.cleaned_data.get("comment")
				data.user = request.user
				data.pack = tour
				data.save()

				return redirect('themedTour:themedsingle', id)
			# else:
			# 	print(form.errors,"====================================")
				
			# 	messages.error(request, "SHEAVSE!")

			# 	return redirect('userProfile:userreservation')
		else:
			form = ThemedReviewForm()

		
		return render(request, 'homepage/homepage.html', {'form': form})

	else:
		return redirect('accounts/login')


def pack_order(request, id):
	pack = ThemedPack.objects.get(id=id)
	context = {
		'pack': pack,
	}
	return render(request, 'themedTour/pack_order.html', context)

 
def get_order(request, id):
	if request.user.is_authenticated:
		pack = ThemedPack.objects.get(id=id)
		if request.method == "POST":
			form = OrderedThemedPackForm(request.POST or None)
			dates = ThemedPackReservation.objects.filter(pack_id=id)
			if form.is_valid():
				#===================Getting dates for loop=================

				get_start_date = datetime.strptime(request.POST.get("order_start_date"),'%Y-%m-%d')
				order_startdate = datetime.date(get_start_date)
				get_end_date = datetime.strptime(request.POST.get("order_end_date"),'%Y-%m-%d')
				order_enddate = datetime.date(get_end_date)

				#====================  end dates  ============================

				order = form.save(commit=False)
				
				for day in range((order_enddate - order_startdate).days+1):
					tourorderdate = order_startdate + timedelta(day)
					for qs in dates:
						if tourorderdate==qs.date:
							check_quantity = qs.quantity-int(request.POST.get("order_travelers"))
							if check_quantity>=0:
								order.user = request.user
								order.pack = pack
							else:
								form = OrderedThemedPackForm()
								return redirect('themedTour:themedsingle', id)


				order.save()
				

				for day in range((order_enddate - order_startdate).days+1):
					tourorderdate = order_startdate + timedelta(day)
					for qs in dates:
						if tourorderdate == qs.date:
							left_quantity = qs.quantity-int(order.order_travelers)
							updated_reservation = ThemedPackReservation.objects.get(pack=qs.pack, date=qs.date)
							updated_reservation.quantity = left_quantity
							updated_reservation.save()
				return redirect('themedTour:thankyou')
			else:
				form = OrderedThemedPackForm()
			return render(request, 'themedTour/pack_single.html', {'form':form})
	else:
		return redirect('themedTour:themedsingle', id)








