from django.urls import path
from . import views

app_name = "components"

urlpatterns = [
    path("about/",views.about_view,name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("faq/",views.faq_view,name="faq"),
    # path("question/",views.faq_question,name="faqQuestion"),
    path('privacy_policy', views.privacy_policy, name='privacyPolicy'),
    path('terms_and_conditions', views.terms_and_conditions, name='termsAndConditions'),
]
