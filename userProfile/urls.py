from django.urls import path
from . import views

app_name = "userProfile"

urlpatterns = [
#customer

    path("customerprofile/<int:id>", views.customer_profile, name="customerProfile"),
    path("ratepartners", views.rate_booky_partners, name="ratepartners"),
    path("reservation", views.UserReservations.as_view(), name="userReservation"),

#supplier

    path('supplierprofile/<int:id>', views.supplier_profile, name='supplierProfile'),
    path('supplierpayments', views.supplier_payments, name='supplierPayments'),
    path('supplieritems', views.supplier_items, name='supplierItems'),

#PDF
    path('supplierpayments/pdf/<int:id>',views.GeneratePdf.as_view(), name='generatePdf'),

#supplier themed pack

    path('supplieritem/<int:id>', views.supplier_item_pack, name='supplierItem'),
    path('supplierpackedit/<int:id>', views.edit_supplier_themed_pack, name='supplierPackEdit'),
    path('editsupplierpackdescription/<int:id>/<int:findex>', views.edit_supplier_themed_pack_description, name='editSupplierPackDescription'),
    path('suppliercalendarprice/<int:id>', views.supplier_price_edit, name='supplierCalendarPrice'),
    path('suppliercalendarquantity/<int:id>', views.supplier_quantity_edit, name='supplierCalendarQuantity'),
    path('supplieraddpack', views.supplier_themed_pack_add, name='supplierAddPack'),
    path('supplierdescriptionadd/<int:id>', views.supplier_themed_pack_description_add, name='supplierDescriptionAdd'),
    path('supplierpackreservation/<int:id>', views.supplier_themed_pack_reservation, name='supplierPackReservation'),

#supplier accomodation

    path('supplieraccommodationadd', views.supplier_accommodation_add, name='supplierAccommodationAdd'),
    path('supplieraccommodationedit/<int:id>', views.supplier_accommodation_edit, name='supplierAccommodationEdit'),

#supplier hotel

    path('supplierhotel/<int:id>', views.supplier_item_hotel, name='supplierHotel'), 
    path('edithotel/<int:acc_id>/<int:hotel_id>', views.edit_hotel_description, name='editHotel'),
    path('supplierhoteladd/<int:id>', views.supplier_hotel_add, name='supplierHotelAdd'),

#supplier apartment

    path('supplierapartment/<int:id>', views.supplier_item_apartment, name='supplierApartment'),
    path('supplierapartmentadd/<int:id>', views.supplier_apartment_add, name='supplierApartmentAdd'),

#supplier car

    path('suppliercar/<int:id>', views.supplier_item_car, name='supplierCar'),
    path('suppliercaradd', views.supplier_car_add, name='supplierCarAdd'),

#supplier other things
    path('roomplanning', views.room_planning, name='roomPlanning'),
    path('supplierlogin', views.supplier_login, name='supplierLogin'),
    # path('themedreview/<int:id>', views.themed_review, name='themedreview'),

]
