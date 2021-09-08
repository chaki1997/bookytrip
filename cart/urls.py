from django.urls import path
from . import views

app_name = "cart"




urlpatterns = [

path('cart/<int:id>/<int:hotel_id>', views.AddToCart.as_view(), name='addcart'),
path('cartremove/<int:product_id>',views.CartRemove.as_view(),name='cartremove'),
path('cartcar/<int:id>', views.AddToCartCar.as_view(), name='addcartcar'),

]