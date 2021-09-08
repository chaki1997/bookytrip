from django.shortcuts import render, redirect
from themedTour.models import ThemedPack, OrderedThemedPack, ThemedDaysDescription, ThemedPackReview
from personalTour.models import AccommodationReview, CarReview, Accommodation, Hotel, Apartment, Car, AccommodationOrder, OrderCar, HotelOrder
from datetime import timedelta, date, datetime
from .models import ThemedPackReservation, Country, FooterDescription, ThemedPackDuration, \
                    ThemedPackVariety, CarMark, City, TermsAndConditions, PrivacyPolicy, DefaultPriceAdd, \
                    SupplierPercentageAdd
from components.models import Faq, Contact, WhyUs, About, Vendor
from components.forms import WhyUsForm, AboutForm, VendorForm
from homepage.models import HomePageDestination, HomePageInterestingFacts
from registration.models import Account
from django.views import View
from .forms import ThemedPackForm, ThemedDaysDescriptionForm, FaqModelForm, FooterForm, \
                    ThemedPackPriceForm, ThemedPackTravelersQuantityForm, ThemedPackReviewForm, \
                    AccommodationReviewForm, CarReviewForm, DashboardOrderedThemedPackForm, AccomodationForm, \
                    HotelForm, ApartmentForm, ThemedPackDurationForm, ThemedPackVarietyForm, \
                    CarMarkForm, CarForm, CityForm, TermsAndConditionsForm, PrivacyPolicyForm, HomePageDestinationForm, \
                    HomePageInterestingFactsForm, DefaultPriceAddForm, SupplierPercentageAddForm
from registration.forms import UserCreationForm, AdminChangeForm
from django.forms.formsets import formset_factory
from registration.forms import UserChangeForm
from django.contrib import messages
# from django_countries import countries


def dashboard(request):

    faq_notificaiton_count    = Faq.objects.filter(notification=False).count()
    themed_pack_review_count  = ThemedPackReview.objects.filter(notification=False).count()
    accomodation_review_count = AccommodationReview.objects.filter(notification=False).count()
    car_review_count          = CarReview.objects.filter(notification=False).count()
    themed_pack_count         = ThemedPack.objects.filter(notification=False).count()
    hotels_count              = Accommodation.objects.filter(accommodation_type="1", notification=False).count()
    apartment_count           = Accommodation.objects.filter(accommodation_type="2", notification=False).count()
    car_count                 = Car.objects.filter(notification=False).count()
    supplier_count            = Account.objects.filter(is_supplier=True, notification=False).count()
    contact_count             = Contact.objects.filter(notification=False).count()

    context = {
        'faq_notificaiton_count':faq_notificaiton_count,
        'themed_pack_review_count':themed_pack_review_count,
        'accomodation_review_count':accomodation_review_count,
        'car_review_count':car_review_count,
        'themed_pack_count':themed_pack_count,
        'hotels_count':hotels_count,
        'apartment_count':apartment_count,
        'car_count':car_count,
        'supplier_count':supplier_count,
        'contact_count':contact_count,
    }

    return render(request, 'adminPanel/dashboard_main.html', context)


# ======================ADMIN PART====================================
# ====================================================================

#=======================Country Part=====================================
def dashboard_country(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'adminPanel/adminPart/dashboard_country.html', context)


def add_country(request):
    if request.method == 'POST':
        countryCode = request.POST.get('country')
        addCountry = Country(country=countryCode)
        addCountry.save()

        return redirect('adminPanel:dashboardCountry')

    return render(request, 'adminPanel/adminPart/dashboard_country_add.html')


def delete_country(request, id):
    country = Country.objects.get(id=id).delete()
    return redirect('adminPanel:dashboardCountry')


def dashboard_city(request, id):
    cities = City.objects.filter(highway=id)
    context = {
        'cities':cities,
    }

    return render(request, 'adminPanel/adminPart/dashboard_cities.html', context)


def dashboard_city_add(request):
    cities = {"Tbilisi":(155, 550), "Rustavi":(145,400)}

    # HTML part
    js_cities = ''
    for i in cities:
        js_cities+= str(i)+ ","
    #=====================
    form = CityForm()
    if request.method=="POST":
        form = CityForm(request.POST, files=request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            if data.city in cities:
                data.x_c = cities[data.city][0]
                data.y_c = cities[data.city][1]
                data.save()
                return redirect('adminPanel:dashboardCities', request.POST.get('highway'))
            else:
                return redirect('adminPanel:dashboardCityAdd')
    context = {
        'form':form,
        'js_cities':js_cities[:-1],
    }

    return render(request, 'adminPanel/adminPart/dashboard_city_add.html', context)


def dashboard_city_single(request, id):
    city = City.objects.get(id=id)
    form = CityForm(instance=city)
    if request.method=='POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:dashboardCitySingle', id)
    context = {
        'city':city,
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_city_single.html', context)


def dashboard_city_delete(request, id):
    id_redirect = City.objects.get(id=id).highway.id
    city = City.objects.get(id=id).delete()

    return redirect('adminPanel:dashboardCities', id_redirect)

#=======================END Country Part=====================================

#=======================Footer Part==========================================

def dashboard_footer(request):
    footer_description = FooterDescription.objects.get(id=1)
    form = FooterForm(instance=footer_description)
    if request.method=="POST":
        form = FooterForm(request.POST, instance=footer_description)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:dashboardFooter',)
    context = {
        'footer_description':footer_description,
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_footer_single.html', context)

#=======================END Footer Part======================================


#=======================Themed Pack Durations================================


def dashboard_themed_pack_durations(request):
    pack_duration = ThemedPackDuration.objects.all()
    context = {
        'pack_duration': pack_duration,
    }

    return render(request, 'adminPanel/adminPart/dashboard_Themed_pack_durations.html', context)


def dashboard_add_themed_pack_durations(request):
    form = ThemedPackDurationForm()
    if request.method == 'POST':
        form = ThemedPackDurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:packDuration')


    return render(request, 'adminPanel/adminPart/dashboard_Themed_pack_duration_add.html', {'form':form})


def delete_duration(request, id):
    pack_duration = ThemedPackDuration.objects.get(id=id).delete()
    return redirect('adminPanel:packDuration')


#=======================END Themed Pack Durations============================


#=======================Themed Pack Varieties Part===========================

def dashboard_pack_varieties(request):
    pack_variety = ThemedPackVariety.objects.all()

    context = {
        'pack_variety': pack_variety,
    }

    return render(request, 'adminPanel/adminPart/Themedpackvarieties.html', context)


def delete_variety(request, id):
    pack_variety = ThemedPackVariety.objects.get(id=id).delete()
    return redirect('adminPanel:packVarieties')



def dashboard_add_pack_varieties(request):
    form = ThemedPackVarietyForm()
    if request.method == 'POST':
        form = ThemedPackVarietyForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('adminPanel:packVarieties')

    return render(request, 'adminPanel/adminPart/dashboard_Themed_pack_varieties_add.html', {'form':form})


#=======================END Themed Pack Varieties Part=======================


#=======================Car Marks========================================


def dashboard_car_marks(request):
    car_marks = CarMark.objects.all()
    print(car_marks)
    context = {
        'car_marks':car_marks,
    }

    return render(request, 'adminPanel/adminPart/dashboard_car_marks.html', context)


def dashboard_car_mark_add(request):
    form = CarMarkForm()
    if request.method=="POST":
        form = CarMarkForm(request.POST or None)
        if form.is_valid():
            form.save()


        return redirect('adminPanel:dashboardCarMarks')

    return render(request, 'adminPanel/adminPart/dashboard_car_mark_add.html',{'form':form})


def delete_car_mark(request, id):
    car_mark = CarMark.objects.get(id=id).delete()
    return redirect('adminPanel:dashboardCarMarks')

#========================END CAR MARKS===================================


def dashboard_terms_and_conditions(request):
    terms_and_conditions = TermsAndConditions.objects.get(id=1)
    form = TermsAndConditionsForm(instance=terms_and_conditions)
    if request.method=="POST":
        form = TermsAndConditionsForm(request.POST, instance=terms_and_conditions)
        if form.is_valid():
            form.save()
    context = {
        'terms_and_conditions':terms_and_conditions,
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_terms_and_conditions.html', context)


def dashboard_privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.get(id=1)
    form = PrivacyPolicyForm(instance=privacy_policy)
    if request.method=="POST":
        form = PrivacyPolicyForm(request.POST, instance=privacy_policy)
        if form.is_valid():
            form.save()
            messages.success(request, 'yochaaaaaaaaaaaaaaaag')
        else:
            messages.error(request, "tinki vinki")
    context = {
        'privacy_policy':privacy_policy,
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_privacy_policy.html', context)

#====================DEFAULT PRICES===================================

def dashboard_default_price(request):
    default_price = DefaultPriceAdd.objects.get(id=1)
    form = DefaultPriceAddForm(instance=default_price)
    if request.method=='POST':
        form = DefaultPriceAddForm(request.POST, instance=default_price)
        if form.is_valid():
            form.save()

            return redirect('adminPanel:dashboardDefaultPrice')
    context = {
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_default_price.html', context)


def dashboard_default_percentage(request):

    percentages = SupplierPercentageAdd.objects.all()

    context = {
        'percentages':percentages,
    }

    return render(request, 'adminPanel/adminPart/dashboard_default_percentage.html', context)


def dashboard_default_percentage_add(request):
    form = SupplierPercentageAddForm()

    if request.method=='POST':
        form = SupplierPercentageAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Modified successfully!!")
            return redirect('adminPanel:dashboardDefaultPercentage')
    context = {
        'form':form,
    }
    return render(request, 'adminPanel/adminPart/dashboard_default_percentage_add.html', context)


def dashboard_default_percentage_edit(request, id):

    percentage = SupplierPercentageAdd.objects.get(id=id)
    form = SupplierPercentageAddForm(instance=percentage)

    if request.method=='POST':
        form = SupplierPercentageAddForm(request.POST, instance=percentage)
        if form.is_valid():
            form.save()
            messages.success(request, "Modified successfully!!")

            return redirect('adminPanel:dashboardDefaultPercentageEdit', id)

    context = {
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_default_percentage_edit.html', context)


def dashboard_default_percentage_delete(request, id):
    percentages = SupplierPercentageAdd.objects.get(id=id).delete()
    return redirect('adminPanel:dashboardDefaultPercentage')

#====================END DEFAULT PRICES===================================

#====================WHY US==============================================

def dashboard_why_us(request):

    why_us = WhyUs.objects.all()
    number_of_content = len(why_us)
    context = {
        'why_us':why_us,
        'number_of_content':number_of_content,
    }

    return render(request, 'adminPanel/adminPart/dashboard_why_us.html', context)


def dashboard_why_us_add(request):

    form = WhyUsForm()

    if request.method=='POST':
        form = WhyUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('adminPanel:dashboardWhyUs')
        
    context = {
        'form':form,
    }
    
    return render(request, 'adminPanel/adminPart/dashboard_why_us_add.html', context)


def dashboard_why_us_edit(request, id):

    why_us = WhyUs.objects.get(id=id)
    form = WhyUsForm(instance=why_us)

    if request.method =='POST':
        form = WhyUsForm(request.POST, request.FILES, instance=why_us)
        if form.is_valid():
            form.save()
            messages.success(request, "Modified successfully!!")
            return redirect('adminPanel:dashboardWhyUsEdit', id)
    context = {
        'why_us':why_us,
        'form':form,
    }
    return render(request, 'adminPanel/adminPart/dashboard_why_us_edit.html', context)


#====================END WHY US==============================================

# ======================END ADMIN PART====================================
# ========================================================================


#=======================USER PART ========================================
#=========================================================================

def dashboard_admins(request):

    admins = Account.objects.filter(is_staff=True)

    context = {
        'admins':admins,
    }

    return render(request, 'adminPanel/dashboardUsers/dashboard_admins.html', context)


def dashboard_suppliers(request):

    suppliers = Account.objects.filter(is_superuser=False, is_supplier=True).order_by('-id')

    supplier_notification_tuple = ()
    notification = 0

    try:
        while suppliers[notification].notification !=True:
            supplier_notification_tuple += (suppliers[notification].id,)
            data = suppliers[notification]
            data.notification = True
            data.save()
            notification += 1

    except IndexError:
        pass

    context = {
        'suppliers':suppliers,
        'supplier_notification_tuple':supplier_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardUsers/dashboard_suppliers.html', context)


def dashboard_customers(request):

    customers = Account.objects.filter(is_superuser=False, is_supplier=False)

    context = {
        'customers':customers,
    }

    return render(request, 'adminPanel/dashboardUsers/dashboard_customers.html', context)


def dashboard_admin_add(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.is_staff = True
            form.save()
            return redirect('adminPanel:admins')
    context = {
        'form': form,
    }
    return render(request, 'adminPanel/dashboardUsers/add_admin.html', context)


def dashboard_admin_edit(request, id):
    user = Account.objects.get(id=id)
    form = AdminChangeForm(instance=user)
    if user.is_staff:
        if request.method == "POST":
            form = AdminChangeForm(request.POST, request.FILES, instance=Account.objects.get(id=id))
            if form.is_valid():
                data = form.save(commit=False)
                data.is_superuser = True
                data.is_staff = True
                data.is_active = True
                data.save()
                return redirect('adminPanel:admins')
    context = {
        'form': form,
        'id': id
    }
    return render(request, "adminPanel/dashboardUsers/editadmin.html", context)


def delete_admin(request, id):
    user = Account.objects.get(id=id).delete()
    return redirect('adminPanel:admins')


def dashboard_supplier_edit(request, id):
    user = Account.objects.get(id=id)
    form = UserChangeForm(instance=user)

    if request.method == "POST":
        form = UserChangeForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('adminPanel:editSupplier', id)
        else:
            print(form.errors)

            
    context = {
        'form':form,
        'user':user,
    }

    return render(request, 'adminPanel/dashboardUsers/editsupplier.html', context)


def dashboard_customer_edit(request, id):
    user = Account.objects.get(id=id)
    form = UserChangeForm(instance=user)

    if request.method == "POST":
        form = UserChangeForm(request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('adminPanel:editCustomer', id)
        else:
            print(form.errors)

            
    context = {
        'form':form,
        'user':user,
    }

    return render(request, 'adminPanel/dashboardUsers/editcustomer.html', context)


#=======================END USER PART ========================================
#=========================================================================


#==========================Themed Pack===================================
#========================================================================


def dashboard_themed_packs(request):

    packs = ThemedPack.objects.all().order_by('-id')
    pack_notification_tuple = ()
    notification = 0

    try:
        while packs[notification].notification !=True:
            pack_notification_tuple += (packs[notification].id,)
            data = packs[notification]
            data.notification = True
            data.save()
            notification += 1

    except IndexError:
        pass

    context = {
        'packs':packs,
        'pack_notification_tuple':pack_notification_tuple,
    }
    
    return render(request, 'adminPanel/dashboardThemedTours/Themed_Pack.html', context)

def dashboard_single_pack(request, id):
    pack = ThemedPack.objects.get(id=id)
    countries = Country.objects.all()
    pack_variety = ThemedPackVariety.objects.all()
    calendar = ThemedPackReservation.objects.filter(pack_id=id)
    form = ThemedPackForm(instance=pack)
    form_price = ThemedPackPriceForm()
    form_quantity = ThemedPackTravelersQuantityForm()
    day_description = ThemedDaysDescription.objects.filter(pack_connect_day=id)
    form_day_description = {}
    for i in range(pack.number_of_days.duration):
        form_day_description[i] = ThemedDaysDescriptionForm(instance=day_description[i])
    context = {
        'pack':pack,
        'countries':countries,
        'pack_variety':pack_variety,
        'calendar':calendar,
        'form':form,
        'form_day_description':form_day_description,
        'form_price':form_price,
        'form_quantity':form_quantity,
    }

    return render(request, 'adminPanel/dashboardThemedTours/edit_themed_pack.html', context)


def edit_themed_pack(request, id):
    if request.method=='POST':
        pack = ThemedPack.objects.get(id=id)
        form = ThemedPackForm(request.POST,files=request.FILES, instance=pack)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "yochaaaaaaaag")
            return redirect('adminPanel:dashboardSinglePack', id)
            
        else:
            print(form.errors)
            messages.error(request, 'vuime')
            return redirect('adminPanel:dashboardSinglePack', id)

    
def edit_themed_pack_description(request, id,findex):
    if request.method=='POST':
        pack = ThemedPack.objects.get(id=id)
        description = ThemedDaysDescription.objects.filter(pack_connect_day=id)

        for i in range(len(description)):
            if i==findex:
                form = ThemedDaysDescriptionForm(request.POST,instance=description[i])

        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect('adminPanel:dashboardSinglePack', id)
    
    
def add_themed_pack(request):
    form = ThemedPackForm()

    if request.method == 'POST':
        form = ThemedPackForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('adminPanel:addThemedDaysDescriptions', data.id)
    

    return render(request, 'adminPanel/dashboardThemedTours/add_Themed_Pack.html', {'form': form})


def add_themed_days_descriptions(request, id):
    # formset
    pack = ThemedPack.objects.get(id=id)
    # formset = ThemedDaysDescriptionFormset()
    themedDaysDescriptionFormSet = formset_factory(ThemedDaysDescriptionForm, extra=pack.number_of_days.duration)

    if request.method == 'POST':
        formset = themedDaysDescriptionFormSet(request.POST or None)
        if formset.is_valid():
            for form in formset:
                # extract name from each form and save
                data = form.save(commit=False)
                # save book instance
                data.pack_connect_day = pack
                data.save()

                # if description:
                #     ThemedDaysDescription(description=description, pack_connect_day=pack).save()
            # once all books are saved, redirect to book list view
            return redirect('adminPanel:themedPackReservation', id)

    formset = themedDaysDescriptionFormSet()

    context = {
        'formset': formset,
        'pack': pack,
    }

    return render(request, 'adminPanel/dashboardThemedTours/addThemedDaysDescriptions.html', context)


def themed_pack_reservation(request, id):
    pack = ThemedPack.objects.get(id=id)

    for day in range((pack.end_date - pack.start_date).days+1):
        # tour_id = ThemedPack.objects.get(id=pack.id)
        quantity = pack.number_of_travelers
        calendar_price = pack.price
        # date_dic[dict_key] = [pack.id, pack.start_date + timedelta(day), calendar_price, quantity]
        reservation = ThemedPackReservation(pack=pack, date=pack.start_date + timedelta(day), quantity=quantity,
                                            calendar_price=calendar_price)
        reservation.save()
    return redirect('adminPanel:dashboardSinglePack', id)


    #==========================Review Themed Pack================================

def themed_pack_review(request):

    themed_pack_reviews = ThemedPackReview.objects.all().order_by('-id',)
    themed_pack_review_notification_tuple = ()
    packs = ThemedPack.objects.all()
    review = 0
    try:
        while themed_pack_reviews[review].notification !=True:
            themed_pack_review_notification_tuple += (themed_pack_reviews[review].id,)
            data = themed_pack_reviews[review]
            data.notification = True
            data.save()
            review += 1

    except IndexError:
        for review in themed_pack_reviews:
            themed_pack_review_notification_tuple += (review,)
            tamuna = review
            tamuna.notification = True
            tamuna.save()
    
    

    context = {
        'themed_pack_reviews': themed_pack_reviews,
        'themed_pack_review_notification_tuple':themed_pack_review_notification_tuple,
        'packs':packs,
    }


    return render(request, 'adminPanel/dashboardThemedTours/Themed_Pack_Reviews.html', context)


def edit_themed_pack_review(request, id):
    themed_pack_review = ThemedPackReview.objects.get(id=id)
    form = ThemedPackReviewForm(instance=themed_pack_review)
    if request.method =="POST":
        form = ThemedPackReviewForm(request.POST, instance=themed_pack_review)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:editThemedPackReview', id)
    context = {
        'themed_pack_review':themed_pack_review,
        'form': form,
    }

    return render(request, 'adminPanel/dashboardThemedTours/change_themed_pack_review.html', context)


def themed_pack_review_delete(request,id):
    themed_pack_review = ThemedPackReview.objects.get(id=id)
    themed_pack_review.delete()
    return redirect('adminPanel:themedPackReview')


    #==========================END OF REVIEW=====================================

    #==========================ORDER THEMED PACK=================================

def themed_pack_orders(request):
    order_packs = OrderedThemedPack.objects.all()
    context = {
        'order_packs':order_packs,
    }

    return render(request, 'adminPanel/dashboardThemedTours/order_themed_packs.html', context)


def themed_pack_order_add(request):
    form = DashboardOrderedThemedPackForm()
    # if request.method == "POST":
    #     form = DashboardOrderedThemedPackForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('adminPanel:themedPackOrder')

    return render(request, 'adminPanel/dashboardThemedTours/add_order_themed_pack.html', {'form':form})


def themed_pack_order_edit(request, id):
    pack_order = OrderedThemedPack.objects.get(id=id)
    form = DashboardOrderedThemedPackForm(instance=pack_order)
    if request.method =="POST":
        form = DashboardOrderedThemedPackForm(request.POST, instance=pack_order)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:editThemedPackOrder', id)
    context = {
        'pack_order': pack_order,
        'form': form,
    }

    return render(request, 'adminPanel/dashboardThemedTours/edit_dashboard_themed_pack.html', context)


    #==========================END ORDER=========================================


    #==========================Themed Pack Calendar Options======================

    #dashboard price edit===============================
def dashboard_price_edit(request, id):
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

        return redirect('adminPanel:dashboardSinglePack', id)

        #End ThemedPack Reservation=====================
    

    #dashboard quantity edit===============================
def dashboard_quantity_edit(request, id):
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

        return redirect('adminPanel:dashboardSinglePack', id)

        #End ThemedPack Reservation=====================





    #==========================END Themed Pack Calendar Options==================

#========================END THEME PACK===================
#=========================================================


#=======================COMPONENTS=======================
    #=======================FAQ===============================

def dashboard_faq(request):
    faqs = Faq.objects.all().order_by('-id',)
    faq_notification_tuple = ()
    faq = 0
    try:
        while faqs[faq].notification != True:
            faq_notification_tuple += (faqs[faq].id,)
            data = faqs[faq]
            data.notification=True
            data.save()
            faq +=1

    except IndexError:
        for faq in faqs:
            faq_notification_tuple += (faq.id,)
            data = faq
            data.notification = True
            data.save()

    context = {
        'faqs':faqs,
        'faq_notification_tuple':faq_notification_tuple,
    }
    return render(request, 'adminPanel/dashboardComponents/FAQ.html', context)


def faq_edit(request,id):
    faq = Faq.objects.get(id=id)
    form = FaqModelForm(instance=faq)
    if request.method =="POST":
        form = FaqModelForm(request.POST,instance=faq)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:dashboardFaq')
    context = {
        'faq':faq,
        'form':form,
    }

    return render(request, 'adminPanel/dashboardComponents/changeFAQ.html', context)

def faq_delete(request,id):

    faq = Faq.objects.get(id=id)
    faq.delete()
    return redirect('adminPanel:dashboardFaq')


def faq_add(request):
    form = FaqModelForm()
    if request.method == "POST":
        form = FaqModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('adminPanel:addFaq')
    return render(request,'adminPanel/dashboardComponents/addfaq.html')


    #=======================END FAQ===============================


    #======================HOME PAGE DESTINATION==============

def home_page_destination(request):
    homepage_destination = HomePageDestination.objects.get(id=1)
    form = HomePageDestinationForm(instance=homepage_destination)

    if request.method=="POST":
        form = HomePageDestinationForm(request.POST, request.FILES, instance=homepage_destination)
        if form.is_valid():
            form.save()

            return redirect('adminPanel:homePageDestination')

    context = {
        'form':form,
    }
    return render(request, 'adminPanel/dashboardComponents/home_page_destination.html', context)




    #======================Interesting Facts====================


def dashboard_interesting_facts(request):

    facts = HomePageInterestingFacts.objects.all()
    number_of_facts = len(facts)

    context = {
        'facts': facts,
        'number_of_facts': number_of_facts,
    }


    return render(request, 'adminPanel/adminPart/dashboard_interesting_facts.html', context)


def interesting_fact_add(request):

    form = HomePageInterestingFactsForm()

    if request.method=='POST':
        form = HomePageInterestingFactsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Here is some creative logo!!")

            return redirect('adminPanel:interestingFacts')

    context = {
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_interesting_fact_add.html', context)


def interesting_fact_edit(request, id):

    fact = HomePageInterestingFacts.objects.get(id=id)
    form = HomePageInterestingFactsForm(instance=fact)

    if request.method=='POST':
        form = HomePageInterestingFactsForm(request.POST, request.FILES, instance=fact)
        if form.is_valid():
            form.save()
            messages.success(request, "Here is some creative logo!!")

            return redirect('adminPanel:interestingFactEdit', id)

    context = {
        'fact':fact,
        'form':form,
    }

    return render(request, 'adminPanel/adminPart/dashboard_interesting_fact_edit.html', context)


    #===================CONTACTS========================

def dashboard_contacts(request):
    contacts = Contact.objects.all().order_by("-id")
    contact_notification_tuple = ()
    notification = 0

    try:
        while contacts[notification].notification !=True:
            contact_notification_tuple += (contacts[notification].id,)
            data = contacts[notification]
            data.notification = True
            data.save()
            notification += 1
    except IndexError:
        pass

    context = {
        'contacts': contacts,
        'contact_notification_tuple':contact_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_contacts.html', context)


def dashboard_contact(request, id):

    contact = Contact.objects.get(id=id)

    context = {
        'contact':contact,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_contact_inner.html', context)


    #===================ABOUT PAGE======================
def dashboard_about(request):

    about_page = About.objects.all()
    number_of_about = len(about_page)

    context = {
        'about_page':about_page,
        'number_of_about':number_of_about,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_about.html', context)


def dashboard_about_add(request):

    form = AboutForm()
    if request.method =='POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Here is some creative logo!!")
            return redirect('adminPanel:dashboardAbout')

    context = {
        'form':form,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_about_add.html', context)


def dashboard_about_edit(request, id):

    about = About.objects.get(id=id)
    form = AboutForm(instance=about)

    if request.method =='POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, "Modified successfully!!")
            return redirect('adminPanel:dashboardAboutEdit', id)

    context = {

        'form':form,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_about_edit.html', context)

    #===================END ABOUT PAGE==================


    #===================VENDORS=========================

def dashboard_vendors(request):

    vendors = Vendor.objects.all().order_by("-id")

    context = {
        'vendors':vendors,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_vendors.html', context)


def dashboard_vendor_add(request):

    form = VendorForm()

    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Here is some creative logo!!")
            return redirect('adminPanel:dashboardVendors')
    context = {
        'form':form,
    }

    return render(request, 'adminPanel/dashboardComponents/dashboard_vendor_add.html', context)


def dashboard_vendor_delete(request, id):
    vendor = Vendor.objects.get(id=id).delete()
    return redirect('adminPanel:dashboardVendors')


    #===================END VENDORS=====================

#=======================END COMPONENTS==================


#======================ORDERS===========================

def supplier_orders(request):
    suppliers = Account.objects.filter(is_supplier=True)
    accommodations = Accommodation.objects.filter(accommodation_type='1')
    hotels = HotelOrder.objects.all()
    context = {
        'hotels':hotels,
        'suppliers':suppliers,
        'accommodations':accommodations,
    }
    return render(request, 'adminPanel/orders/supplier_orders.html', context)
class Suplier_orders(View):
    template_name_unpaid =  'adminPanel/orders/supplier_orders.html'
    template_name_paid = 'adminPanel/orders/supplier_orders_paid.html'
    def get(self,request,**kwargs):
        #print(kwargs)
        suppliers = Account.objects.filter(is_supplier=True)
        accommodations = Accommodation.objects.filter(accommodation_type='1')
        slug=kwargs['slug']
        if slug=='unpaid':
            hotels = HotelOrder.objects.filter(payment_status='unpaid')
            context = {
            'hotels': hotels,
            'suppliers': suppliers,
            'accommodations': accommodations,
            }
            return render(request, self.template_name_unpaid, context)
        elif slug == 'paid':
            hotels = HotelOrder.objects.filter(payment_status='paid')
            context = {
                'hotels': hotels,
                'suppliers': suppliers,
                'accommodations': accommodations,
            }
            return render(request, self.template_name_paid, context)
    def post(self,request,id,**kwargs):
        print('shemovida',id)

        order = HotelOrder.objects.filter(id=id)
        print(order)

        order.update(payment_status='paid')

        return redirect('adminPanel:supplierOrders',slug='unpaid')



#======================END ORDERS=======================


#========================Personal Tour====================
#=========================================================

    #===================Accomodation==========================

        #===================APARTMENT=============================

def dashboard_apartments(request):
    
    apartments = Accommodation.objects.filter(accommodation_type="2").order_by('-id')
    apartment_notification_tuple = ()
    notification = 0

    try:
        while apartments[notification].notification !=True:
            apartment_notification_tuple += (apartments[notification].id,)
            data = apartments[notification]
            data.notification = True
            data.save()
            notification += 1

    except IndexError:
        pass


    context = {
        'apartments':apartments,
        'apartment_notification_tuple':apartment_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardAccomodation/apartments.html',context)


def dashboard_apartment_single(request, id):
    accomodation = Accommodation.objects.get(id=id)
    accomodation_form = AccomodationForm(instance=accomodation)
    apartment = Apartment.objects.get(apartment_name=id)
    apartment_form = ApartmentForm(instance=apartment)

    context = {
        'accomodation': accomodation,
        'accomodation_form': accomodation_form,
        'apartment': apartment,
        'apartment_form':apartment_form,
    }


    return render(request, 'adminPanel/dashboardAccomodation/dashboard_apartment_single.html', context)


def dashboard_accommodation_apartment_edit(request, id):
    if request.method=='POST':
        accomodation = Accommodation.objects.get(id=id)
        form = AccomodationForm(request.POST, files=request.FILES, instance=accomodation)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            if data.accommodation_type=="1":
                return redirect('adminPanel:dashboardHotelSingle', id)
            else:
                return redirect('adminPanel:dashboardApartmentSingle', id)


def dashboard_apartment_edit(request, id):
    if request.method=='POST':
        apartment = Apartment.objects.get(apartment_name=id)
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect('adminPanel:dashboardApartmentSingle', id)


def dashboard_apartment_add(request, id):
    accomodation_apartment = Accommodation.objects.get(id=id)
    form = ApartmentForm()
    if request.method=="POST":
        form = ApartmentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.apartment_name = accomodation_apartment
            data.save()

            return redirect('adminPanel:dashboardApartment')

    context = {
        'accomodation_apartment':accomodation_apartment,
        'form':form,
    }

    return render(request, 'adminPanel/dashboardAccomodation/apartment_add.html', context)


        #==========================END APARTMENT==========================


        #=========================HOTEL==================================

def dashboard_hotels(request):

    hotels = Accommodation.objects.filter(accommodation_type="1").order_by('-id')
    hotel_notification_tuple = ()
    notification = 0

    try:
        while hotels[notification].notification !=True:
            hotel_notification_tuple += (hotels[notification].id,)
            data = hotels[notification]
            data.notification = True
            data.save()
            notification += 1

    except IndexError:
        pass

    context = {
        'hotels':hotels,
        'hotel_notification_tuple':hotel_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardAccomodation/hotels.html', context)


def dashboard_hotel_single(request, id):
    calendar_start_date = (datetime.today() - timedelta(days=16)).strftime('%Y-%m-%d')
    calendar_end_date = (datetime.today() + timedelta(days=15)).strftime('%Y-%m-%d')
    if request.method=='POST':
        calendar_start_date = request.POST.get('calendar_start_date')
        calendar_end_date = request.POST.get('calendar_end_date')
    accomodation = Accommodation.objects.get(id=id)
    accomodation_form = AccomodationForm(instance=accomodation)
    hotels = Hotel.objects.filter(hotel_name=id)
    hotel_tuple = ()
    for hotel in hotels:
        hotel_tuple+= (HotelForm(instance=hotel),)

    context = {
        'accomodation': accomodation,
        'accomodation_form': accomodation_form,
        'hotel_tuple':hotel_tuple,
        'calendar_start_date':calendar_start_date,
        'calendar_end_date':calendar_end_date,
    }


    return render(request, 'adminPanel/dashboardAccomodation/dashboard_hotel_single.html', context)


def dashboard_hotel_edit(request, id):
    if request.method=='POST':
        hotel = Hotel.objects.get(hotel_name=id)
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'saved')
            return redirect('adminPanel:dashboardHotelSingle', id)


def dashboard_hotel_delete(request, id):
    hotel = Accommodation.objects.get(id=id).delete()
    return redirect('adminPanel:dashboardHotels')


def dashboard_accomodation_add(request):
    form = AccomodationForm()
    if request.method=="POST":
        form = AccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            if data.accommodation_type=="1":
                return redirect('adminPanel:dashboardHotelAdd', data.id)
            else:
                return redirect('adminPanel:dashboardApartmentAdd', data.id)
        


    return render(request, 'adminPanel/dashboardAccomodation/accomodation_add.html',{'form':form})


def dashboard_hotel_add(request, id):
    accomodation_hotel = Accommodation.objects.get(id=id)
    form = HotelForm()
    if request.method=="POST":
        form = HotelForm(request.POST)
        print(form)
        if form.is_valid():
            print('valide')
            #data = form.save(commit=False)
            #data.hotel_name = accomodation_hotel
            #data.save()
        else:
            print('form is invalide')
        
        #return redirect('adminPanel:dashboardHotelDescriptionAdd', data.id)

    context = {
        'form':form,
        'accomodation_hotel':accomodation_hotel,
    }

    return render(request, 'adminPanel/dashboardAccomodation/hotel_add.html', context)


        #======================END HOTEL==================================

            #===================Accomodation Review=================

def dashboard_accomodation_reviews(request):

    dashboard_accomodation = AccommodationReview.objects.all().order_by('-id')
    accomodation_review_notification_tuple = ()
    review = 0
    try:
        while dashboard_accomodation[review].notification !=True:
            accomodation_review_notification_tuple += (dashboard_accomodation[review].id,)
            data = dashboard_accomodation[review]
            data.notification = True
            data.save()
            review += 1

    except IndexError:
        for review in dashboard_accomodation:
            accomodation_review_notification_tuple += (review.id,)
            data = review
            data.notification = True
            data.save()

    context = {
        'dashboard_accomodation':dashboard_accomodation,
        'accomodation_review_notification_tuple':accomodation_review_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardAccomodation/accomodation_reviews.html', context)


def dashboard_accomodation_review_edit(request, id):
    
    accomodation_review = AccommodationReview.objects.get(id=id)
    form = AccommodationReviewForm(instance=accomodation_review)
    if request.method =="POST":
        form = AccommodationReviewForm(request.POST, instance=accomodation_review)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:accomodationReviewEdit', id)
    context = {
        'accomodation_review':accomodation_review,
        'form':form,

    }

    return render(request, 'adminPanel/dashboardAccomodation/accomodation_review_edit.html',context)


def delete_accommodation_review(request, id):
    accommodation_review = AccommodationReview.objects.get(id=id).delete()
    return redirect('adminPanel:carReview')


        #===================Accomodation Review End=============

    #==================END of Accomodation====================

    #===================Car================================

def dashboard_cars(request):

    cars = Car.objects.all().order_by('-id')
    car_notification_tuple = ()
    review = 0
    try:
        while cars[review].notification !=True:
            car_notification_tuple += (cars[review].id,)
            data = cars[review]
            data.notification = True
            data.save()
            review += 1

    except IndexError:
        pass

    context = {
        'cars': cars,
        'car_notification_tuple':car_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardCars/cars.html', context)


def dashboard_car_add(request):
    form = CarForm()

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.notification = True
            data.save()

        return redirect('adminPanel:dashboardCars')

    return render(request, 'adminPanel/dashboardCars/car_add.html', {'form':form})


def dashboard_car_edit(request, id):
    car = Car.objects.get(id=id)
    car_order_dates = OrderCar.objects.filter(car=id)
    form = CarForm(instance=car)
    if request.method =="POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:dashboardCarEdit', id)
    context = {
        'car':car,
        'form':form,
        'car_order_dates':car_order_dates,
    }

    return render(request, 'adminPanel/dashboardCars/car_edit.html', context)

        #===================Car review=========================

def dashboard_car_review(request):

    dashboard_car = CarReview.objects.all().order_by('-id')
    car_review_notification_tuple = ()
    review = 0
    try:
        while dashboard_car[review].notification !=True:
            car_review_notification_tuple += (dashboard_car[review].id,)
            data = dashboard_car[review]
            data.notification = True
            data.save()
            review += 1

    except IndexError:
        pass


    context = {
        'dashboard_car':dashboard_car,
        'car_review_notification_tuple':car_review_notification_tuple,
    }

    return render(request, 'adminPanel/dashboardCars/dashboard_car_reviews.html', context)


def dashboard_car_review_edit(request, id):

    car_review = CarReview.objects.get(id=id)
    form = CarReviewForm(instance=car_review)
    if request.method =="POST":
        form = CarReviewForm(request.POST, instance=car_review)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:carReviewEdit', id)
    context = {
        'car_review':car_review,
        'form':form,

    }

    return render(request, 'adminPanel/dashboardCars/dashboard_car_review_edit.html', context)


def delete_car_review(request, id):
    car_review = CarReview.objects.get(id=id).delete()
    return redirect('adminPanel:carReview')


        #===================Car review End====================

    #=======================END OF CAR===========================

#========================Personal Tour End==================