from django.urls import path
from . import views

app_name = "themedTour"


urlpatterns = [
    path("packchoice", views.themed_tour, name="packchoice"),
    path("thankyou", views.thankyou, name="thankyou"),

    path("singlepack/<int:id>", views.themed_single, name="themedsingle"),
    path('themedreview/<int:id>', views.themed_review, name='themedreview'),
    path("packorder/<int:id>", views.pack_order, name='packorder'),
    path("getorder/<int:id>", views.get_order, name='getorder'),
]
