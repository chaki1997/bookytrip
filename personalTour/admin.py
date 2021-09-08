from django.contrib import admin
from .models import Accommodation, Hotel, Apartment, AccommodationReview, Car, CarReview,\
     AccomodationCheckout, AccommodationOrder, OrderCar,HotelOrder,Order
# Register your models here.
admin.site.register(Accommodation)
admin.site.register(Hotel)
admin.site.register(Apartment)
admin.site.register(AccommodationReview)
admin.site.register(Car)
admin.site.register(CarReview)
admin.site.register(AccomodationCheckout)
admin.site.register(AccommodationOrder)
admin.site.register(OrderCar)
admin.site.register(HotelOrder)
admin.site.register(Order)



