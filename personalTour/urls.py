from django.urls import path
from . import views

app_name = "personalTour"




urlpatterns = [

    path('accomodationmiddle', views.Middle_accommodation.as_view(), name='accomodationMiddle'),

    path("archiveaccommodation", views.Archive_accommodation.as_view(), name="archiveaccommodation"),
    path("archiveaccommodation/<slug:slug>", views.Archive_accommodation.as_view(), name="archiveaccommodation"),

    path("singleaccommodation/<int:id>", views.Single_accommodation.as_view(), name="singleaccommodation"),
    path('accommodationreview/<int:id>', views.accommodation_review, name='accommodationreview'),
    path("archivecar", views.archive_car, name="archivecar"),
    path("singlecar/<int:id>", views.single_car, name="singlecar"),
    path('carreview/<int:id>', views.car_review, name='carreview'),
    path('personalcheckout/', views.Personaltour_checkout.as_view(), name='personalCheckout'),
    path('checkoutcar/<int:id>', views.car_order, name='checkoutCar'),
]
