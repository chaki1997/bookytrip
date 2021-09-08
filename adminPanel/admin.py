from django.contrib import admin
from .models import Country, FooterDescription, ThemedPackReservation, ThemedPackDuration, \
                    ThemedPackVariety, ThemedPackTravelersQuantity,ThemedPackPrice,City, \
                    TermsAndConditions, PrivacyPolicy, DefaultPriceAdd, CarMark

admin.site.register(Country)
admin.site.register(FooterDescription)
admin.site.register(ThemedPackReservation)
admin.site.register(ThemedPackDuration)
admin.site.register(ThemedPackVariety)
admin.site.register(ThemedPackTravelersQuantity)
admin.site.register(ThemedPackPrice)
admin.site.register(City)
admin.site.register(TermsAndConditions)
admin.site.register(PrivacyPolicy)
admin.site.register(DefaultPriceAdd)
admin.site.register(CarMark)
