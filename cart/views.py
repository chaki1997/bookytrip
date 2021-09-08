from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .cart import Cart
from personalTour.models import Hotel,Accommodation,Car
from adminPanel.models import Country, CarMark, City
# Create your views here.
from cart.context_processors import cart as scart
class AddToCart(View):
    def post(self,request,id,hotel_id):
        print('shemovida')
        print(request.POST.get('capacity_value'))
        #if request.POST.get('capacity_value') !=None:
        dinamic_capacity = request.POST.get('capacity_value')


        cart = Cart(request)
        #print(cart.cart)
        #print(request.session['cart_calcs'])
        hotel = get_object_or_404(Hotel,id=hotel_id)
        #print('hotel capacity',hotel.capacity)
        #print('es',request.session['cities'],hotel_id,id,hotel.hotel_name.city.city)
        #parse session cities to get start_date and end_date
        city=hotel.hotel_name.city.city
        print(request.session['cities'])
        for i in request.session['cities']:
            if i['title'] == city:
                start_date=i['start_date']
                end_date=i['end_date']
            print(i['title'])
        cart.add(product=hotel,start_date=start_date,end_date=end_date,hotel_id=id,
                 dinamic_capacity=dinamic_capacity,override_quantity=True,car_id=0)

        return redirect(f'/singleaccommodation/{id}')

class CartRemove(View):

    def post(self,request,product_id):
        cart = Cart(request)
        hotel = get_object_or_404(Hotel,id=product_id)
        cart.remove(hotel)

        print('removeshi shemovida')
        if request.user.is_authenticated:
            print('if',request.POST)
            url = request.POST.get('next')
            return redirect(url)
        else:
            print('else',request.POST.get('next'))
            url = request.POST.get('next')
            return redirect(url)

from personalTour.forms import CarOrderForm
class AddToCartCar(View):
    form_class = CarOrderForm
    def post(self,request,id):
        print(id)
        print('shemovida ad to cart carshi')
        car = get_object_or_404(Car, id=id)
        print(car)
        form=self.form_class(request.POST)
        print(form)
        if form.is_valid():

            print(form['car_order_start_date'])
            print(form['car_order_end_date'])
            print(form.cleaned_data)
            data = form.cleaned_data
            cart = Cart(request)
            cart.add(product=car, start_date=data['car_order_start_date'].strftime("%Y-%m-%d"), end_date=data['car_order_end_date'].strftime("%Y-%m-%d"),
                     hotel_id=0,
                     car_id=id,
                     dinamic_capacity=1, override_quantity=True)

        return redirect(f'/singlecar/{id}')
