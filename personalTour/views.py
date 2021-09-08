from django.shortcuts import render, redirect
from .models import Accommodation, Car, AccommodationReview, CarReview, AccomodationCheckout,\
                     AccommodationOrder, OrderCar, Hotel, HotelOrder,Order
from adminPanel.models import FooterDescription, City
from .forms import AccommodationReviewForm, CarReviewForm, AccommodationOrderForm, CarOrderForm,RoomAddToCartForm
from django.forms.formsets import formset_factory
from django.views import View
from adminPanel import models
from django.db.models import Q
import json
from cart.context_processors import cart
from cart.cart import Cart
class Middle_accommodation(View):
    template_name = 'personalTour/personalmiddle.html'

    def get(self,request):
        cities = City.objects.all()
        #store da to session with ajax for navigate and query (cities navigators)
        if request.is_ajax:
            data = list(request.GET.keys())
            print(data)

            if len(data) != 0:

                data = json.loads(data[0])
                print(data)

                request.session['cities'] =data['cities']
                request.session.modified = True
                print('----------------------------------------------------------------------',data['cities'])
                print('session',request.session['cities'])






        context = {

            'cities': cities,
        }

        return render(request, self.template_name, context)
    def post(self,request):
        cities = City.objects.all()
        context = {

            'cities': cities,
        }

        return render(request, self.template_name, context)






class Archive_accommodation(View):
    template_name = 'personalTour/archive_accommodation.html'

    def get(self,request,**kwargs):

        if 'slug' in kwargs.keys():
            city = kwargs['slug']
        else:
            city = request.session['cities'][0]['title']

        city = City.objects.get(city__exact=city)
        #retrive data from session and collect it in list(cities)
        data_list = request.session['cities']
        cntx_city_list = []
        for i in data_list:
            cntx_city_list.append(i['title'])
        cntx_city_list=list(set(cntx_city_list))
        accommodations = Accommodation.objects.filter(city=city)
        print(cntx_city_list)

        context = {
            'accommodations': accommodations,
            'cities': cntx_city_list
        }
        #print(cart(request)['cart'].cart)
        return render(request,self.template_name,context)
    def post(self, request):
        return render(request,self.template_name,{})





class Single_accommodation(View):
    template_name = 'personalTour/accommodation_single.html'
    form_class = RoomAddToCartForm
    def get(self,request,id):
        accommodation = Accommodation.objects.get(id=id)
        hotels = Hotel.objects.filter(hotel_name=accommodation)
        reviews = AccommodationReview.objects.filter(accommodation_id=id)

        for i in request.session['cities']:
            if i['title'] == accommodation.city.city:
                print(i)
                start_date = i['start_date']
                end_date = i['end_date']
               # print(i['start_date'],i['end_date'])
        #print(accommodation.city.city)
        for hotel in hotels:
            print(hotel.picture1)
            orders=HotelOrder.objects.filter(hotel=hotel,hotel_order_start_date__lte=end_date,hotel_order_end_date__gte = start_date)


            print('start',orders)
            if len(orders)>=5:

                hotels = Hotel.objects.filter(hotel_name=accommodation).exclude(id=hotel.id)
                #hotels = hotels.filter(id=hotel.id).delete()

        print(hotels)

        full_url = request.build_absolute_uri()
        url_list = full_url.split('/')
        url = ''
        #print(request.session['cart_calcs'])
        for i in url_list[3:]:
            url = url + i + '/'
        url=url[:-1]
        print(url)
        #city = City.objects.get(city__exact=city)
        data_list = request.session['cities']
        #print(request.session['cities'])
        #print(request.build_absolute_uri())
        cntx_city_list = []
        for i in data_list:
            cntx_city_list.append(i['title'])
        cntx_city_list = list(set(cntx_city_list))
        #print(request.session['room_order'])
        #accommodations = Accommodation.objects.filter(city=city)
        #print(hotels)
        context = {

            'accommodation': accommodation,
            'reviews': reviews,
            'hotels': hotels,

            'id':id,
            'cities': cntx_city_list

        }
        return render(request,self.template_name,context)
    def post(self,request,id):
        accommodation = Accommodation.objects.get(id=id)
        hotels = Hotel.objects.filter(hotel_name=accommodation)
        reviews = AccommodationReview.objects.filter(accommodation_id=id)

        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #print(data['room'])
            room = data['room']
            #print(room)
        room_order = request.POST

        hotelID = room_order['price']

        hotel = Hotel.objects.get(hotel_name=accommodation,id=hotelID)
        print(hotel)
        print(accommodation)

        order_dict = {'accommodationID':accommodation.id,'hotelID':hotel.id}
        print(request.session.get('room_order'))
        if len(request.session['room_order'])==0:
            request.session['room_order'] = [order_dict]
        else:
            saved_list = request.session['room_order']
            saved_list.append(order_dict)
            #request.session['room_order']=saved_list
            request.session.modified = True

        context = {

            'accommodation': accommodation,
            'reviews': reviews,
            'hotels': hotels,
            'forms': self.form_class,
            'id': id

        }
        return render(request, self.template_name, context)
'''
def single_accommodation(request, id):
    accommodation = Accommodation.objects.get(id=id)
    hotels = Hotel.objects.filter(hotel_name=accommodation)
    reviews = AccommodationReview.objects.filter(accommodation_id=id)


    context = {

        'accommodation': accommodation,
        'reviews': reviews,
        'hotels':hotels,

    }

    return render(request, 'personalTour/accommodation_single.html', context)
'''

def accommodation_review(request, id):
    if request.user.is_authenticated:
        tour = Accommodation.objects.get(id=id)
        if request.method == 'POST':
            form = AccommodationReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.accommodation = tour
                data.save()

                return redirect('personalTour:singleaccommodation', id)
        else:
            form = AccommodationReviewForm()

        return render(request, 'personalTour/accommodation_single.html', {'form': form})
    else:
        return redirect('accounts/login')






def archive_car(request):
    cars = Car.objects.all()
    data_list = request.session['cities']

    cntx_city_list = []
    for i in data_list:
        cntx_city_list.append(i['title'])
    cntx_city_list = list(set(cntx_city_list))


    context = {

        'cars': cars,
        'cities':cntx_city_list,

    }

    return render(request, 'personalTour/archive_car.html', context)


def single_car(request, id):
    car = Car.objects.get(id=id)
    reviews = CarReview.objects.filter(car_id=id)
    form = CarOrderForm()
    data_list = request.session['cities']
    cntx_city_list = []
    for i in data_list:
        cntx_city_list.append(i['title'])
    cntx_city_list = list(set(cntx_city_list))

 
    context = {

        'car': car,
        'reviews': reviews,
        'form':form,
        'cities':cntx_city_list,
    }

    return render(request, 'personalTour/single_car.html', context)


def car_review(request, id):
    if request.user.is_authenticated:
        tour = Car.objects.get(id=id)
        if request.method == 'POST':
            form = CarReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.car = tour
                data.save()

                return redirect('personalTour:singlecar', id)
        else:
            form = CarReviewForm()

        return render(request, 'personalTour/single_car.html', {'form': form})
    else:
        return redirect('accounts/login')


def personaltour_checkout(request):
    try:
        gotten_ids = request.GET.get('roomsId').split()

    except:
        gotten_ids = []
    if len(gotten_ids)>0:
        hotels = Hotel.objects.filter(id__in=gotten_ids)
    else:
        hotels = []
    print(Cart(request))
    print(cart(request)['cart'].cart.items)
    cntx_list = []


    for key,value in cart(request)['cart'].cart.items():
        print(key)
        #acomodation = Accommodation.objects.get(id=value['hotel_id'])
        #hotel = Hotel.objects.get(id=key,hotel_name=acomodation)
        #cntx_list.append((hotel,acomodation))
    context = {
        # 'formset':formset,
        # 'room_dict':room_dict,
        # 'total_price':total_price,
        'hotels':cntx_list,


    }
    return render(request, 'personalTour/order_pack_personal.html', context)

class Personaltour_checkout(View):
    template_name = 'personalTour/order_pack_personal.html'
    def get(self,request):
        cntx_list = []
        car_cntx_list = []
        print('------------cart----------', cart(request)['cart'].cart)
        for key, value in cart(request)['cart'].cart.items():
            #print(value)
            start_date=value['start_date']
            end_date=value['end_date']
            print('key------',key)
            if 'car' not in key:
                acomodation = Accommodation.objects.get(id=value['hotel_id'])
                hotel = Hotel.objects.get(id=key, hotel_name=acomodation)
                cntx_list.append((hotel, acomodation,start_date,end_date))
            else:
                car = Car.objects.get(id=value['car_id'])
                car_cntx_list.append((car,start_date,end_date))
        context = {
            # 'formset':formset,
            # 'room_dict':room_dict,
            # 'total_price':total_price,
            'hotels': cntx_list,
            'cars':car_cntx_list,
        }
        return render(request, self.template_name, context)
    def post(self,request):
        print('shemovida')
        cntx_list = []
        user=request.user

        if len(cart(request)['cart'].cart.keys()) != 0:
            order = Order.objects.create(user=user)
            order = Order.objects.get(id=order.id)
            for key, value in cart(request)['cart'].cart.items():
                if 'car' not in key:
                    print(value)
                    start_date = value['start_date']
                    end_date = value['end_date']
                    acomodation = Accommodation.objects.get(id=value['hotel_id'])
                    hotel = Hotel.objects.get(id=key, hotel_name=acomodation)
                    print(hotel)
                    cntx_list.append((hotel, acomodation, start_date, end_date))

                    HotelOrder.objects.create(user=user,
                                      supplier=acomodation.user,
                                      hotel=hotel,
                                      order=order,
                                      order_price=hotel.price,
                                      hotel_shared_room_capacity=2,
                                      order_travalers=2,
                                      hotel_order_start_date=start_date,
                                      hotel_order_end_date=end_date)
                else:
                    start_date = value['start_date']
                    end_date = value['end_date']
                    car=Car.objects.get(id=value['car_id'])
                    OrderCar.objects.create(
                        user = user,
                        car = car,
                        car_order_start_date = start_date,
                        car_order_end_date = end_date,
                        order = order,

                    )





        context = {
            'hotels': cntx_list,
        }
        return render(request, 'personalTour/thankyoupage.html', context)




def car_order(request, id):
    car = Car.objects.get(id=id)
    car_orders = OrderCar.objects.filter(car=id)
    car_order_dates = []
    for order in car_orders:
        car_order_dates.append((str(order.car_order_start_date), str(order.car_order_end_date)))
    form = CarOrderForm()
    print(car_order_dates)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CarOrderForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = request.user
                data.car = car
                car_order_dates.append((str(data.car_order_start_date), str(data.car_order_end_date)))
                car_order_dates.sort()
                order_index = car_order_dates.index((str(data.car_order_start_date), str(data.car_order_end_date)))
                print(car_order_dates)
                if order_index == 0:
                    if car_order_dates[order_index][1] < car_order_dates[order_index+1][0]:
                        data.save()
                elif order_index == len(car_order_dates):
                    if  car_order_dates[order_index][0] > car_order_dates[order_index-1][1]:
                        data.save()   
                else:
                    if car_order_dates[order_index][0] > car_order_dates[order_index-1][1] and car_order_dates[order_index][1] < car_order_dates[order_index+1][0]:
                        data.save()

                return redirect('themedTour:thankyou')        

    context = {
        'car':car,
        'form':form,
    }

    return render(request, 'personalTour/checkout_car.html', context)
