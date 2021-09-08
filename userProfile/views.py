from django.shortcuts import render, redirect
from themedTour.models import OrderedThemedPack, ThemedPack, ThemedPackReview, ThemedDaysDescription
from adminPanel.models import Country, FooterDescription, ThemedPackReservation
from personalTour.models import Accommodation, AccommodationReview, Car, CarReview, Hotel, AccommodationOrder, Apartment, OrderCar,HotelOrder
from .forms import ThemedReviewForm, SupplierThemedPackForm, SupplierAccomodationForm, SupplierHotelForm, \
                    SupplierApartmentForm, SupplierCarForm, SupplierThemedDaysDescriptionForm
from adminPanel.forms import ThemedDaysDescriptionForm, ThemedPackPriceForm, ThemedPackTravelersQuantityForm
import datetime
from datetime import timedelta, date, datetime
from django.contrib import messages
from django.db.models import Avg
from django.forms.formsets import formset_factory
from registration.models import Account
from registration.forms import UserChangeForm
from django.views import View

def customer_profile(request, id):
    user = Account.objects.get(id=id)
    form = UserChangeForm(instance=user)

    if request.method == "POST":
        form = UserChangeForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            data = form.save(commit=False)
            data.is_supplier = False
            data.is_active = True
            data.save()
            
            return redirect('userProfile:customerProfile', id)
        else:
            print(form.errors)

    context = {
        'form':form,
        'user':user,
    }

    return render(request, 'userProfile/customer_profile.html', context)


def user_reservation(request):

    ordered_packs = OrderedThemedPack.objects.filter(user=request.user)
    packs = ThemedPack.objects.all()
    current_time=date.today()
   
    context = {
        
        'ordered_packs':ordered_packs,
        'current_time': current_time,
    }
    return render(request, 'userProfile/reservation.html', context)

class UserReservations(View):
    def get(self,request):
        return render(request, 'userProfile/reservation.html', {})


def rate_booky_partners(request):

    context = {
        
    }
    return render(request, 'userProfile/rate_booky_partners.html', context)


# def themed_review(request, id):
#     tour = ThemedPack.objects.get(id=id)
#     print("vax chemi")
#     if request.method == 'POST':
#         form = ThemedReviewForm(request.POST or None)
#         print("valodia")
#         if form.is_valid():
#             print("vinki")
#             data = form.save(commit=False)
#             data.user = request.user
#             data.pack = tour
#             data.save()

#             return redirect('userProfile:userreservation', id)

#         else:
#             print("tinki")
#             messages.error(request, "SHEAVSE!")

#             return redirect('userProfile:userreservation', id)

#     else:
#         form = ThemedReviewForm()

#     return render(request, 'userProfile/reservation.html', {'form': form})


def supplier_profile(request, id):
    user = Account.objects.get(id=id)
    form = UserChangeForm(instance=user)

    if request.method == "POST":
        form = UserChangeForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            data = form.save(commit=False)
            data.is_supplier = True
            data.is_active = True
            data.save()
            
            return redirect('userProfile:supplierProfile', id)
        else:
            print(form.errors)
       
    context = {
        'form':form,
        'user':user,
    }

    return render(request, 'userProfile/supplier_profile.html', context)

import pdfkit
def supplier_payments(request):
    print(request.user)

    unpaid_hotels=HotelOrder.objects.filter(supplier=request.user,payment_status='unpaid')
    paid_hotels = HotelOrder.objects.filter(supplier=request.user, payment_status='paid')

    context = {'unpaid_hotels': unpaid_hotels,
               'paid_hotels': paid_hotels}




    return render(request, 'userProfile/my_payments.html',context)

from django.http import HttpResponse
from django.views.generic import View
from datetime import date
from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        obj = HotelOrder.objects.get(id=id, supplier=self.request.user, payment_status='paid')

        data = {
            'obj':obj,
             'today': date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }


        print(obj)
        pdf = render_to_pdf('userProfile/invoice.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename=%s" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
        #return HttpResponse(pdf, content_type='application/pdf')



def supplier_items(request):
    supplier_themed_packs = ThemedPack.objects.filter(user=request.user)
    themed_packs = {}
    for i in supplier_themed_packs:
        try:
            themed_packs[i] = round(ThemedPackReview.objects.filter(pack=i).aggregate(Avg('stars')).get('stars__avg'),1)
        except TypeError:
            themed_packs[i] = 0
    try:
        avarange_themed_pack_stars = sum(themed_packs.values())/len(themed_packs)
    except ZeroDivisionError:
        avarange_themed_pack_stars = 0

    print(themed_packs)
    supplier_accommodations = Accommodation.objects.filter(user=request.user, accommodation_type="1")
    accommodations = {}
    for i in supplier_accommodations:
        nom = i.hotel_set.filter(hotel_name=i)
        try:
            accommodations[i] = ((round(AccommodationReview.objects.filter(accommodation=i).aggregate(Avg('stars')).get('stars__avg'),1)),nom)
        except TypeError:
            accommodations[i] = (0, nom)

    try:
        avarange_accommodation_stars = tuple(accommodations.values())[0][0]/len(accommodations)
    except:
        avarange_accommodation_stars = 0


    supplier_appartment = Accommodation.objects.filter(user=request.user, accommodation_type="2")
    apartments = {}
    print(apartments)
    for i in supplier_appartment:
        toa = i.apartment_set.get(apartment_name=i)
        try:
            apartments[i] = ((round(AccommodationReview.objects.filter(accommodation=i).aggregate(Avg('stars')).get('stars__avg'),1)), toa)
        except TypeError:
            apartments[i] = (0, toa)
    print(apartments)
    try:
        avarange_apartment_stars = tuple(apartments.values())[0][0]/len(apartments)
    except:
        avarange_apartment_stars = 0


    supplier_cars = Car.objects.filter(user=request.user)
    cars = {}
    for i in supplier_cars:
        try:
            cars[i] = round(CarReview.objects.filter(car=i).aggregate(Avg('stars')).get('stars__avg'),1)
        except TypeError:
            cars[i] = 0
    try:
        avarange_car_stars = sum(cars.values())/len(cars)
    except ZeroDivisionError:
        avarange_car_stars = 0
    if len(apartments)==0:
        apartments = False
    if len(cars)==0:
        cars = False
    if len(themed_packs)==0:
        themed_packs = False
    if len(accommodations)==0:
        accommodations = False
    print(apartments)
    context = {
        'themed_packs':themed_packs,
        'accommodations':accommodations,
        'apartments':apartments,
        'cars':cars,
        'avarange_themed_pack_stars':avarange_themed_pack_stars,
        'avarange_accommodation_stars':avarange_accommodation_stars,
        'avarange_apartment_stars':avarange_apartment_stars,
        'avarange_car_stars':avarange_car_stars,
    }

    return render(request, 'userProfile/my_items.html', context)

#====================THEMED PACK========================================
def supplier_item_pack(request, id):
    supplier_themed_pack = ThemedPack.objects.get(id=id)
    form = SupplierThemedPackForm(instance=supplier_themed_pack)
    day_description = ThemedDaysDescription.objects.filter(pack_connect_day=id)
    form_day_description = {}
    for i in range(supplier_themed_pack.number_of_days.duration):
        form_day_description[i] = ThemedDaysDescriptionForm(instance=day_description[i])
    calendar = ThemedPackReservation.objects.filter(pack_id=id)
    form_price = ThemedPackPriceForm()
    form_quantity = ThemedPackTravelersQuantityForm()
    context = {
        'supplier_themed_pack':supplier_themed_pack,
        'form':form,
        'form_day_description':form_day_description,
        'calendar':calendar,
        'form_price':form_price,
        'form_quantity':form_quantity,
    }

    return render(request, 'userProfile/themed_pack/edit_my_pack.html', context)


def edit_supplier_themed_pack(request, id):
    if request.method=='POST':
        pack = ThemedPack.objects.get(id=id)
        form = SupplierThemedPackForm(request.POST,files=request.FILES, instance=pack)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
                
            return redirect('userProfile:supplierItem', id)


def edit_supplier_themed_pack_description(request, id,findex):
    if request.method=='POST':
        pack = ThemedPack.objects.get(id=id)
        description = ThemedDaysDescription.objects.filter(pack_connect_day=id)

        for i in range(len(description)):
            if i==findex:
                form = ThemedDaysDescriptionForm(request.POST,instance=description[i])

        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect('userProfile:supplierItem', id)


def supplier_price_edit(request, id):
    pack = ThemedPack.objects.get(id=id)

    #ThemedPackPriceForm part===========================

    if request.method=='POST':
        form = ThemedPackPriceForm(request.POST)
        prices = ThemedPackReservation.objects.filter(pack_id=id)

        if form.is_valid():
            #===================Getting dates for loop=================

            get_start_date = datetime.strptime(request.POST.get("price_start_date"),'%Y-%m-%d')
            price_startdate = datetime.date(get_start_date)
            get_end_date = datetime.strptime(request.POST.get("price_end_date"),'%Y-%m-%d')
            price_enddate = datetime.date(get_end_date)

            #====================  end dates  ============================
            data = form.save(commit=False)

            for day in range((price_enddate - price_startdate).days+1):
                tourpricedate = price_startdate + timedelta(day)
                for qs in prices:
                    if tourpricedate==qs.date:
                            data.connect_pack_price = pack
            
            data.save()
    #Saved ThemedPackPriceForm Part========================


        #Edit ThemedPack Reservation=====================
        for day in range((price_enddate - price_startdate).days+1):
            tourpricedate = price_startdate + timedelta(day)
            for qs in prices:
                if tourpricedate == qs.date:
                    new_price = data.dynamic_price
                    updated_reservation = ThemedPackReservation.objects.get(pack=qs.pack, date=qs.date, quantity=qs.quantity,)
                    updated_reservation.calendar_price = new_price
                    updated_reservation.save()

        return redirect('userProfile:supplierItem', id)


def supplier_quantity_edit(request, id):
    pack = ThemedPack.objects.get(id=id)

    #ThemedPackPriceForm part===========================

    if request.method=='POST':
        form = ThemedPackTravelersQuantityForm(request.POST)
        calendar_quantity = ThemedPackReservation.objects.filter(pack_id=id)

        if form.is_valid():
            #===================Getting dates for loop=================

            get_start_date = datetime.strptime(request.POST.get("quantity_start_date"),'%Y-%m-%d')
            quantity_startdate = datetime.date(get_start_date)
            get_end_date = datetime.strptime(request.POST.get("quantity_end_date"),'%Y-%m-%d')
            quantity_enddate = datetime.date(get_end_date)

            #====================  end dates  ============================
            data = form.save(commit=False)

            for day in range((quantity_enddate - quantity_startdate).days+1):
                tourquantitydate = quantity_startdate + timedelta(day)
                for qs in calendar_quantity:
                    if tourquantitydate==qs.date:
                        data.connect_pack_quantity = pack
            
            data.save()
    #Saved ThemedPackPriceForm Part========================


        #Edit ThemedPack Reservation=====================
        for day in range((quantity_enddate - quantity_startdate).days+1):
            tourquantitydate = quantity_startdate + timedelta(day)
            for qs in calendar_quantity:
                if tourquantitydate == qs.date:
                    new_quantity = data.dynamic_quantity
                    updated_reservation = ThemedPackReservation.objects.get(pack=qs.pack, date=qs.date, calendar_price=qs.calendar_price)
                    updated_reservation.quantity = new_quantity
                    updated_reservation.save()

        return redirect('userProfile:supplierItem', id)


def supplier_themed_pack_add(request):

    form = SupplierThemedPackForm()

    if request.method=="POST":
        form = SupplierThemedPackForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            return redirect('userProfile:supplierDescriptionAdd', data.id)

    return render(request, 'userProfile/themed_pack/supplier_themed_pack_add.html', {'form':form})


def supplier_themed_pack_description_add(request, id):
    pack = ThemedPack.objects.get(id=id)
    themedDaysDescriptionFormSet = formset_factory(SupplierThemedDaysDescriptionForm, extra=pack.number_of_days.duration)
    
    if request.method == 'POST':
        formset = themedDaysDescriptionFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                data = form.save(commit=False)
                data.pack_connect_day = pack
                data.save()

            return redirect('userProfile:supplierPackReservation', id)
    formset = themedDaysDescriptionFormSet()

    context = {
        'id':id,
        'formset':formset,
    }
    
    return render(request, 'userProfile/themed_pack/supplier_themed_pack_description_add.html', context)


def supplier_themed_pack_reservation(request, id):
    pack = ThemedPack.objects.get(id=id)

    for day in range((pack.end_date - pack.start_date).days+1):

        quantity = pack.number_of_travelers
        calendar_price = pack.price
        reservation = ThemedPackReservation(pack=pack, date=pack.start_date + timedelta(day), quantity=quantity,
                                            calendar_price=calendar_price)
        reservation.save()
    return redirect('userProfile:supplierItem', id)

#====================THEMED PACK END===================================

#===================ACCOMMODATION ====================================

def supplier_accommodation_edit(request, id):
    if request.method=='POST':
        accomodation = Accommodation.objects.get(id=id, user=request.user)
        form = SupplierAccomodationForm(request.POST, files=request.FILES, instance=accomodation)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            if data.accommodation_type=="1":
                return redirect('userProfile:supplierHotel', id)
            else:
                return redirect('userProfile:supplierApartment', id)


def supplier_accommodation_add(request):
    form = SupplierAccomodationForm()
    if request.method=="POST":
        form = SupplierAccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            if data.accommodation_type=="1":
                return redirect('userProfile:supplierHotelAdd', data.id)
            else:
                return redirect('userProfile:supplierApartmentAdd', data.id)
                
    return render(request, 'userProfile/personal_tour/supplier_accommodation_add.html', {'form':form})


#====================HOTEL=============================================

def supplier_item_hotel(request, id):
    calendar_start_date = (datetime.today() - timedelta(days=16)).strftime('%Y-%m-%d')
    calendar_end_date = (datetime.today() + timedelta(days=15)).strftime('%Y-%m-%d')
    if request.method=='POST':
        calendar_start_date = request.POST.get('calendar_start_date')
        calendar_end_date = request.POST.get('calendar_end_date')

    accomodation = Accommodation.objects.get(id=id, user=request.user)
    accomodation_form = SupplierAccomodationForm(instance=accomodation)

    hotels = Hotel.objects.filter(hotel_name=id)
    hotel_tuple = ()
    for hotel in hotels:
        hotel_tuple += (SupplierHotelForm(instance=hotel),)


    cop_context = zip(hotel_tuple,hotels)
    context = {
        'accomodation': accomodation,
        'accomodation_form': accomodation_form,
        'hotels': hotels,
        'hotel_tuple':cop_context,
        'calendar_start_date':calendar_start_date,
        'calendar_end_date':calendar_end_date,
    }


    return render(request, 'userProfile/personal_tour/supplier_hotel_single.html', context)

from django.shortcuts import get_object_or_404
def edit_hotel_description(request, **kwargs):
    if request.method=='POST':
        accommodation_hotel = Accommodation.objects.get(id=kwargs['acc_id'])
        #hotel = Hotel.objects.get(hotel_name=accommodation_hotel)
        hotel = get_object_or_404(Hotel,hotel_name=accommodation_hotel,id=kwargs['hotel_id'])
        print(kwargs)
        form = SupplierHotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, 'saved')
            return redirect('userProfile:supplierHotel', kwargs['acc_id'])


def supplier_hotel_add(request, id):
    accommodation_hotel = Accommodation.objects.get(id=id)
    form = SupplierHotelForm()
    if request.method=="POST":
        form = SupplierHotelForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.hotel_name = accommodation_hotel
            data.save()
            messages.success(request, 'saved')
        return redirect('userProfile:supplierItems')

    context = {
        'form': form,
    }

    return render(request, 'userProfile/personal_tour/supplier_hotel_add.html', context)

#=======================APARTMENT==========================================


def supplier_item_apartment(request, id):
    accomodation = Accommodation.objects.get(id=id)
    accomodation_form = SupplierAccomodationForm(instance=accomodation)
    apartment = Apartment.objects.get(apartment_name=id)
    apartment_form = SupplierApartmentForm(instance=apartment)

    context = {
        'accomodation': accomodation,
        'accomodation_form': accomodation_form,
        'apartment': apartment,
        'apartment_form':apartment_form,
    }

    return render(request, 'userProfile/personal_tour/edit_my_apartment.html', context)


def supplier_apartment_add(request, id):
    accommodation_apartment = Accommodation.objects.get(id=id)
    form = SupplierApartmentForm()
    if request.method=="POST":
        form = SupplierApartmentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.apartment_name = accommodation_apartment
            data.save()

            return redirect('userProfile:supplierItems')

    context = {
        'accommodation_apartment':accommodation_apartment,
        'form':form,
    }


    return render(request, 'userProfile/personal_tour/supplier_apartment_add.html', context) 


#=================CAR======================================


def supplier_item_car(request, id):
    car = Car.objects.get(id=id)
    car_order_dates = OrderCar.objects.filter(car=id)
    form = SupplierCarForm(instance=car)
    if request.method =="POST":
        form = SupplierCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('userProfile:supplierCar', id)

    context = {
        'car':car,
        'form':form,
        'car_order_dates':car_order_dates,
    }

    return render(request, 'userProfile/personal_tour/edit_my_car.html', context)


def supplier_car_add(request):
    form = SupplierCarForm()

    if request.method=='POST':
        form = SupplierCarForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            messages.success(request, 'successfully saved!')
            return redirect('userProfile:supplierItems')

    context = {
        'form':form,
    }

    return render(request, 'userProfile/personal_tour/supplier_car_add.html', context)



#=================CAR END======================================

def room_planning(request):

    return render(request, 'userProfile/room_planning_calendar.html')


def supplier_login(request):

    return render(request, 'userProfile/login.html')
