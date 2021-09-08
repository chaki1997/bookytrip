from django.urls import path
from . import views

app_name = "registration"

urlpatterns = [
    path('signup', views.sign_up, name='signUp'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('login_redirect/<slug:email>', views.login_redirect, name='loginRedirect'),
]
