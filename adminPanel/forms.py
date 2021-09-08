from django import forms
from themedTour.models import ThemedPack, ThemedDaysDescription, ThemedPackReview, OrderedThemedPack
from personalTour.models import AccommodationReview, CarReview, Accommodation, Hotel, Apartment, Car
from components.models import Faq
from .models import FooterDescription, Country, ThemedPackVariety, ThemedPackDuration, \
                    ThemedPackPrice, ThemedPackTravelersQuantity, CarMark, City, TermsAndConditions, \
                    PrivacyPolicy, DefaultPriceAdd, SupplierPercentageAdd
from homepage.models import HomePageDestination, HomePageInterestingFacts
from registration.models import Account

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('highway', 'city', 'city_video')
    
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'map_input'}))


class FooterForm(forms.ModelForm):

    class Meta:
        model = FooterDescription
        fields = ('address', 'email', 'phoneKA', 'phoneEN', 'phoneFR',
                 'phoneAZ', 'phoneDE', 'phoneES', 'phoneHY', 'phoneIT', 'phoneRU', 'description',)
    
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control',}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control',}))
    phoneKA = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneEN = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneFR = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneAZ = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneDE = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneES = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneHY = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneIT = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    phoneRU = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))


class ThemedPackDurationForm(forms.ModelForm):

    class Meta:
        model = ThemedPackDuration
        fields = ('duration',)

    duration = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))


class ThemedPackVarietyForm(forms.ModelForm):

    class Meta:
        model = ThemedPackVariety
        fields = ('pack_variety',)

    pack_variety = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))


class CarMarkForm(forms.ModelForm):

    class Meta:
        model = CarMark
        fields = ('car_mark',)

    car_mark = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class TermsAndConditionsForm(forms.ModelForm):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'
    
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control','id': 'editor'}))

    
class PrivacyPolicyForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
    
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'editor'}))
    

class DefaultPriceAddForm(forms.ModelForm):
    class Meta:
        model = DefaultPriceAdd
        fields = ('add_price',)
    
    add_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))


class SupplierPercentageAddForm(forms.ModelForm):
    class Meta:
        model = SupplierPercentageAdd
        fields = '__all__'

    supplier   = forms.ModelChoiceField(queryset=Account.objects.filter(is_supplier=True))
    percentage = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))


class FaqModelForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ('question',
                'question_type',
                'answer',
                'permition',
                )


class HomePageDestinationForm(forms.ModelForm):
    class Meta:
        model = HomePageDestination
        fields = '__all__'

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'footer_textarea form-control', 'id': 'editor', 'maxlength':'20'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text', 'maxlength':'330'}))
    video = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept':"video/mp4"}))


class HomePageInterestingFactsForm(forms.ModelForm):
    class Meta:
        model = HomePageInterestingFacts
        fields = "__all__"

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'footer_textarea form-control', 'id': 'editor', 'maxlength':'30'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text', 'maxlength':'256'}))
    image = forms.FileField(widget=forms.ClearableFileInput())


class ThemedPackForm(forms.ModelForm):

    class Meta:
        model = ThemedPack
        fields = ('user','pack_name', 'description', 'country', 'price', 'picture1', 'picture2',
                    'small_video', 'big_video', 'trip_variety', 'number_of_travelers',
                    'number_of_days', 'start_date', 'end_date', 'permission')

    pack_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id': "editor"}))
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))
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
                                                        'type':'date', 'id':'textfield9'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control',
                                                     'type':'date', 'id':'textfield10'}))
    permission = forms.BooleanField(label = 'Display on front-end', widget=forms.CheckboxInput(attrs={'class':'', 'id':'permition'}))

    # def __init__(self, *args, **kwargs):
    #     if kwargs.get('instance'):
    #         initial = kwargs.setdefault('initial', {})
    #         if kwargs['instance'].country.all():
    #             initial['country']= kwargs['instance'].country.all()[0]
    #         else:
    #             initial['country']=None
    #     forms.ModelForm.__init__(self, *args, **kwargs)


class ThemedDaysDescriptionForm(forms.ModelForm):
    class Meta:
        model = ThemedDaysDescription
        fields = ('description',)

    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))

    
class ThemedPackPriceForm(forms.ModelForm):
    class Meta:
        model = ThemedPackPrice
        fields = ('price_start_date','price_end_date','dynamic_price')

    dynamic_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    price_start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control',
                                                             'type':'date', 'id':'textfield9'}))
    price_end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control',
                                                            'type':'date', 'id':'textfield10'}))


class ThemedPackTravelersQuantityForm(forms.ModelForm):
    class Meta:
        model = ThemedPackTravelersQuantity
        fields = ('quantity_start_date','quantity_end_date','dynamic_quantity')

    dynamic_quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control',}))
    quantity_start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    quantity_end_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))


class ThemedPackReviewForm(forms.ModelForm):
    class Meta:
        model = ThemedPackReview
        fields = ('comment', 'stars', 'permition')

    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','id':'comment'}))
    stars = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id':'stars'}))
    permition = forms.BooleanField(label = 'Display on front-end', widget=forms.CheckboxInput(attrs={'class':'', 'id':'permition'}))


class AccommodationReviewForm(forms.ModelForm):
    class Meta:
        model = AccommodationReview
        fields = ('comment','permition')

    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','id':'comment'}))
    permition = forms.BooleanField(label = 'Display on front-end', widget=forms.CheckboxInput(attrs={}))


class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = ('comment','permition')

    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','id':'comment'}))

    permition = forms.BooleanField(label = 'Display on front-end', widget=forms.CheckboxInput(attrs={'class':'', 'id':'permition'}))


class DashboardOrderedThemedPackForm(forms.ModelForm):

    class Meta:
        model = OrderedThemedPack
        fields = ('__all__')

    order_start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    order_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    order_travelers = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AccomodationForm(forms.ModelForm):

    class Meta:
        model = Accommodation
        fields = ('__all__')

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
    permission = forms.BooleanField(required=False, label = 'Display on front-end', widget=forms.CheckboxInput(attrs={'class':'', 'id':'permition',}))


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        exclude = ('hotel_name',)

    room_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Independent room'),
                                                             ('2', 'Shared room'),
                                                             ('3', 'Private room')]))
    bed_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Twin'),
                                                            ('2', 'Double'),
                                                            ('3', 'Triple'),
                                                            ('4', 'Shared'),]))
    family = forms.BooleanField(widget=forms.CheckboxInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'min':'0'}))
    WiFi_connection = forms.BooleanField(widget=forms.CheckboxInput())
    parking = forms.BooleanField(widget=forms.CheckboxInput())
    bar = forms.BooleanField(widget=forms.CheckboxInput())
    pool = forms.BooleanField(widget=forms.CheckboxInput())
    number_of_rooms = forms.IntegerField(widget=forms.NumberInput(attrs={
                                        'class': 'form-control', 'min': '0'
                                        }))
    picture1 = forms.FileField(widget=forms.ClearableFileInput())
    picture2 = forms.FileField(widget=forms.ClearableFileInput())
    picture3 = forms.FileField(widget=forms.ClearableFileInput())
    picture4 = forms.FileField(widget=forms.ClearableFileInput())
    picture5 = forms.FileField(widget=forms.ClearableFileInput())


class ApartmentForm(forms.ModelForm):

    class Meta:
        model = Apartment
        exclude = ('apartment_name', 'availability', 'city')

    choice_of_apartment = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Studio'),('2', 'F1'),('3', 'F2'),
                                                            ('4', 'F3'),('5', 'F4'),('6', 'villa'),]))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}))


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('notification',)

    destination = forms.ModelChoiceField(queryset=Country.objects.all())
    pick_up_location = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Airport'),('2', 'Hotel'),('3', 'Agency'),]))
    car_types = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control',}),
                                                 choices = ([('1', 'Coupe'),('2', 'Sedan'),('3', 'Van'),]))
    mark = forms.ModelChoiceField(queryset=CarMark.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'min':'0'}))
    number_of_sits = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}))
    picture1 = forms.FileField(widget=forms.ClearableFileInput())
    picture2 = forms.FileField(widget=forms.ClearableFileInput())
    permission = forms.BooleanField(required=False, label = 'Display on front-end', widget=forms.CheckboxInput(attrs={'class':'', 'id':'permition'}))



