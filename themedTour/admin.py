from django.contrib import admin
from .models import ThemedPack, ThemedDaysDescription, ThemedPackReview, OrderedThemedPack


admin.site.register(ThemedPack)
admin.site.register(ThemedDaysDescription)
admin.site.register(ThemedPackReview)
admin.site.register(OrderedThemedPack)