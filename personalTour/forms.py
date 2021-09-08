from django import forms
from .models import AccommodationReview, CarReview, AccommodationOrder, OrderCar


class AccommodationReviewForm(forms.ModelForm):
    class Meta:
        model = AccommodationReview
        fields = ('comment',)



class RoomAddToCartForm(forms.Form):
    room = forms.CharField(max_length=20,required=False, widget=forms.TextInput(attrs={'class':"room"}))




# class RoomOrderForm(forms.ModelForm):
#     class Meta:
#         model = RoomOrder
#         fields = ('room_order_start_date', 'room_order_end_date')
    
#     room_order_start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker',  'type': 'text', }))
#     room_order_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker',  'type': 'text'}))

class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ('comment',)


class AccommodationOrderForm(forms.ModelForm):
    class Meta:
        model = AccommodationOrder
        fields = ('accomodation_order_start_date', 'accomodation_order_end_date')

    accomodation_order_start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker',  'type': 'text'}))
    accomodation_order_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datepicker',  'type': 'text'}))


class CarOrderForm(forms.ModelForm):

    class Meta:
        model = OrderCar
        fields = ('car_order_start_date', 'car_order_end_date')

    car_order_start_date = forms.DateField(
                                           widget=forms.DateInput(attrs={'class': 'form-control order_input_form', 'type': 'date'}))
    car_order_end_date = forms.DateField(
                                         widget=forms.DateInput(attrs={'class': 'form-control order_input_form', 'type': 'date'}))


