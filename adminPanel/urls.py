from django.urls import path
from . import views

app_name = "adminPanel"


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
#adminpart url 
    path('dashboardcountry', views.dashboard_country, name='dashboardCountry'),
    path('deletecountry/<int:id>', views.delete_country, name='deleteCountry'),
    path('addcountry', views.add_country, name='addCountry'),
    path('dashboardcities/<int:id>', views.dashboard_city, name='dashboardCities'),
    path('dashboardcityadd', views.dashboard_city_add, name='dashboardCityAdd'),
    path('dashboardcitysingle/<int:id>', views.dashboard_city_single, name='dashboardCitySingle'),
    path('dashboardcitydelete/<int:id>', views.dashboard_city_delete, name='dashboardCityDelete'),

    path('dashboardfooter', views.dashboard_footer, name='dashboardFooter'),

    path('dashboardtermsandconditions', views.dashboard_terms_and_conditions, name='dashboardTermsAndConditions'),

    path('dasbhoardprivacypolicy', views.dashboard_privacy_policy, name='dashboardPrivacyPolicy'),

    path('packduration', views.dashboard_themed_pack_durations, name='packDuration'),
    path('addpackduration', views.dashboard_add_themed_pack_durations, name='AddpackDuration'),
    path('deletepackduration/<int:id>', views.delete_duration, name='deletePackDuration'),

    path('packvarieties', views.dashboard_pack_varieties, name='packVarieties'),
    path('packvarietiesadd', views.dashboard_add_pack_varieties, name='packVarietiesAdd'),
    path('deletevarieties/<int:id>', views.delete_variety, name='deleteVarieties'),

    path('dashboardcarmarks', views.dashboard_car_marks, name='dashboardCarMarks'),
    path('dashboardcarmarkadd', views.dashboard_car_mark_add, name='dashboardCarMarkAdd'),
    path('deletecarmark/<int:id>', views.delete_car_mark, name='deleteCarMark'),

    path('dashboarddefaultprice', views.dashboard_default_price, name='dashboardDefaultPrice'),
    path('dashboarddefaultpercentage', views.dashboard_default_percentage, name='dashboardDefaultPercentage'),
    path('dashboarddefaultpercentageadd', views.dashboard_default_percentage_add,
                                          name='dashboardDefaultPercentageAdd'),
    path('dashboarddefaultpercentageedit/<int:id>', views.dashboard_default_percentage_edit,
                                                    name='dashboardDefaultPercentageEdit'),
    path('dashboarddefaultpercentagedelete/<int:id>', views.dashboard_default_percentage_delete,
                                                      name='dashboardDefaultPercentageDelete'),


    path('dashboardwhyus', views.dashboard_why_us, name='dashboardWhyUs'),
    path('dashboardwhyusadd', views.dashboard_why_us_add, name='dashboardWhyUsAdd'),
    path('dashboardwhyusedit/<int:id>', views.dashboard_why_us_edit, name='dashboardWhyUsEdit'),
#adminpart end

#user url

    path('admins', views.dashboard_admins, name='admins'),
    path('suppliers', views.dashboard_suppliers, name='suppliers'),
    path('customers', views.dashboard_customers, name='customers'),

    path('addadmin', views.dashboard_admin_add, name='addAdmin'),
    path('editadmin/<int:id>', views.dashboard_admin_edit, name="editAdmin"),
    path('editsupplier/<int:id>', views.dashboard_supplier_edit, name='editSupplier'),
    path('editcustomer/<int:id>', views.dashboard_customer_edit, name='editCustomer'),
    path('deleteadmin/<int:id>', views.delete_admin, name='deleteAdmin'),

#user end

#components

    path('dashboardfaq', views.dashboard_faq, name='dashboardFaq'),
    path('editfaq/<int:id>', views.faq_edit, name='editFaq'),
    path('deletefaq/<int:id>',views.faq_delete, name='deleteFaq'),
    path('addfaq',views.faq_add,name='addFaq'),

    path('homepagedestination', views.home_page_destination, name='homePageDestination'),

    path('interestingfacts', views.dashboard_interesting_facts, name='interestingFacts'),
    path('interestingfactadd', views.interesting_fact_add, name='interestingFactAdd'),
    path('interestingfactedit/<int:id>', views.interesting_fact_edit, name='interestingFactEdit'),


    path('dashboardcontacts', views.dashboard_contacts, name='dashboardContacts'),
    path('dashboardcontact/<int:id>', views.dashboard_contact, name='dashboardContact'),

    path('dashboardabout', views.dashboard_about, name='dashboardAbout'),
    path('dashboardaboutadd', views.dashboard_about_add, name='dashboardAboutAdd'),
    path('dashboardaboutedit/<int:id>', views.dashboard_about_edit, name='dashboardAboutEdit'),

    path('dashboardvendors', views.dashboard_vendors, name='dashboardVendors'),
    path('dashboardvendoradd', views.dashboard_vendor_add, name='dashboardVendorAdd'),
    path('dashboardvendordelete/<int:id>', views.dashboard_vendor_delete, name='dashboardVendorDelete'),
#components end

#orders

    path('supplier_orders/<slug:slug>', views.Suplier_orders.as_view(), name='supplierOrders'),
    path('supplier_orders/<slug:slug>/<int:id>', views.Suplier_orders.as_view(), name='supplierOrdersPost'),

#end orders

    path('dashboardpacks', views.dashboard_themed_packs, name='dashboardPacks'),
    path('dashboardsinglepack/<int:id>', views.dashboard_single_pack, name='dashboardSinglePack'),
    path('editpack/<int:id>', views.edit_themed_pack, name='editPack'),
    path('editpackdescription/<int:id>/<int:findex>', views.edit_themed_pack_description, 
                                                      name='editPackDescription'),
    path('addpack', views.add_themed_pack, name='addPack'),
    path('addthemeddaysdescriptions/<int:id>', views.add_themed_days_descriptions, name='addThemedDaysDescriptions'),
    path('themedpackreservation/<int:id>', views.themed_pack_reservation, name='themedPackReservation'),

    path('priceedit/<int:id>', views.dashboard_price_edit, name='priceEdit'),
    path('quantityedit/<int:id>', views.dashboard_quantity_edit, name='quantityEdit'),

    path('themedpackreview', views.themed_pack_review, name='themedPackReview'),
    path('editthemedpackreview/<int:id>', views.edit_themed_pack_review, name='editThemedPackReview'),
    path('deletethemedpackreview/<int:id>', views.themed_pack_review_delete, name='deleteThemedPackReview'),

    path('themedpackorder', views.themed_pack_orders, name='themedPackOrder'),
    path('addthemedpackorder', views.themed_pack_order_add, name='addThemedPackOrder'),
    path('editthemedpackorder/<int:id>', views.themed_pack_order_edit, name='editThemedPackOrder'),

    path('dashboardapartment', views.dashboard_apartments, name='dashboardApartment'),
    path('dashboardapartmentsingle/<int:id>', views.dashboard_apartment_single, name='dashboardApartmentSingle'),
    path('dashboardaccommodationapartmentedit<int:id>', views.dashboard_accommodation_apartment_edit,
                                                        name='dashboardAccommodationApartmentEdit'),
    path('dashboardapartmentedit<int:id>', views.dashboard_apartment_edit, name='dashboardApartmentEdit'),

    path('dashboardhotels', views.dashboard_hotels, name='dashboardHotels'),
    path('dashboardhotelsingle/<int:id>', views.dashboard_hotel_single, name='dashboardHotelSingle'),
    path('dashboardhoteledit<int:id>', views.dashboard_hotel_edit, name='dashboardHotelEdit'),
    path('dashboardhoteldelete/<int:id>', views.dashboard_hotel_delete, name='dashboardHotelDelete'),

    path('dashboardaccomodationadd', views.dashboard_accomodation_add, name='dashboardAccomodationAdd'),
    path('dashboardhoteladd/<int:id>', views.dashboard_hotel_add, name='dashboardHotelAdd'),
    path('dashboardapartmentadd/<int:id>', views.dashboard_apartment_add, name='dashboardApartmentAdd'),


    path('accomodationreview', views.dashboard_accomodation_reviews, name='accomodationReview'),
    path('accomodationreviewedit/<int:id>', views.dashboard_accomodation_review_edit, name='accomodationReviewEdit'),

    path('carreview', views.dashboard_car_review, name='carReview'),
    path('carreviewedit/<int:id>', views.dashboard_car_review_edit, name='carReviewEdit'),
    path('carreviewdelete<int:id>', views.delete_car_review, name='carReviewDelete'),

    path('dashboardcars', views.dashboard_cars, name='dashboardCars'),
    path('dashboardcaradd', views.dashboard_car_add, name='dashboardCarAdd'),
    path('dashboardcaredit/<int:id>', views.dashboard_car_edit, name='dashboardCarEdit'),


]
