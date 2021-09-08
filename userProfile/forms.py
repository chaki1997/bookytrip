from django import forms
from themedTour.models import ThemedPackReview, ThemedPack, ThemedDaysDescription
from adminPanel.models import Country, ThemedPackVariety, ThemedPackDuration, CarMark
from personalTour.models import Accommodation, Hotel, Apartment, Car

class SupplierThemedPackForm(forms.ModelForm):

    class Meta:
        model = ThemedPack
        fields = ('pack_name', 'description', 'country', 'price', 'picture1', 'picture2',
                    'small_video', 'big_video', 'trip_variety', 'number_of_travelers',
                    'number_of_days', 'start_date', 'end_date',)

    pack_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}))
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min':'0'}))
    picture1 = forms.FileField(widget=forms.ClearableFileInput())
    picture2 = forms.FileField(widget=forms.ClearableFileInput())
    small_video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept':"video/mp4"}))
    big_video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept':"video/mp4"}))
    trip_variety = forms.ModelChoiceField(queryset=ThemedPackVariety.objects.all())
    number_of_travelers = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                choices = ([('1','1'), ('2','2'),('3','3'), ('4','4'),
                                                        ('5','5'), ('6','6'), ('7','7'), ('8','8'),
                                                            ('9','9'), ('10','10')]))
    number_of_days = forms.ModelChoiceField(queryset=ThemedPackDuration.objects.all())
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control',
                                                       'type':'date', 'id':'textfield9,'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control',
                                                     'type':'date', 'id':'textfield10'}))


class SupplierThemedDaysDescriptionForm(forms.ModelForm):
    class Meta:
        model = ThemedDaysDescription
        fields = ('description',)

    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))


class SupplierAccomodationForm(forms.ModelForm):

    class Meta:
        model = Accommodation
        exclude = ('user', 'permission', 'notification')

    identification_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    presentation_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    destination = forms.ModelChoiceField(queryset=Country.objects.all())
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'min':'0'}))
    picture1 = forms.FileField(widget=forms.ClearableFileInput())
    picture2 = forms.FileField(widget=forms.ClearableFileInput())
    picture3 = forms.FileField(widget=forms.ClearableFileInput())
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept':"video/mp4"}))
    accommodation_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1','Hotel'), ('2','Apartment')]))



class SupplierHotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        exclude = ('hotel_name',)


class SupplierApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        exclude = ('apartment_name', 'availability',)

    choice_of_apartment = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Studio'),('2', 'F1'),('3', 'F2'),
                                                            ('4', 'F3'),('5', 'F4'),('6', 'villa'),]))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min':'0'}))



class SupplierCarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('permission', 'user', 'notification')

    destination = forms.ModelChoiceField(queryset=Country.objects.all())
    pick_up_location = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Airport'),('2', 'Hotel'),
                                                            ('3', 'Agency'),]))
    car_types = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Coupe'),('2', 'Sedan'),
                                                            ('3', 'Van'),]))
    mark = forms.ModelChoiceField(queryset=CarMark.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'min':'0'}))
    number_of_sits = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min':'0'}))
    picture1 = forms.FileField(widget=forms.ClearableFileInput())
    picture2 = forms.FileField(widget=forms.ClearableFileInput())


class ThemedReviewForm(forms.ModelForm):
    class Meta:
        model = ThemedPackReview
        fields = ('comment',)


