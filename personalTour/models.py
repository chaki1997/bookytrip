from django.db import models
from adminPanel.models import Country, CarMark, City
from django.core.validators import MaxValueValidator
from registration.models import Account


class Accommodation(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=256)
    identification_number = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    presentation_text = models.TextField(blank=True, null=True)
    destination = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=256)
    picture1 = models.ImageField(upload_to='images/accomodation', default='images/brand-2.jpg')
    picture2 = models.ImageField(upload_to='images/accomodation', default='images/brand-2.jpg',
                                 null=True, blank=True)
    picture3 = models.ImageField(upload_to='images/accomodation', default='images/brand-2.jpg',
                                 null=True, blank=True)
    video = models.FileField(upload_to="accomodationvideos")
    ACCOMODATION_TYPES = (
        ("1", 'Hotel'),
        ("2", 'Apartment'),
    )
    accommodation_type = models.CharField(max_length=256, choices=ACCOMODATION_TYPES)
    permission = models.BooleanField(default=False, blank=True)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Accommodation'


class Hotel(models.Model):
    type=models.CharField(max_length=10,default='hotel')
    hotel_name = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    ROOM_TYPES = (
        ('1', 'Independent room'),
        ('2', 'Shared room'),
        ('3', 'Private room'),
        ('4', 'Custom'),
    )
    room_type = models.CharField(max_length=256, choices=ROOM_TYPES, null=True, blank=True)
    BED_TYPE= (
        ('1', 'Twin'),
        ('2', 'Double'),
        ('3', 'Triple'),
        ('4', 'Suite'),
        ('5', 'Suite deluxe'),
        ('6', 'Triple'),
        ('7', 'Shared'),
   
    )
    bed_type = models.CharField(max_length=256, choices=BED_TYPE, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    family = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    WiFi_connection = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    number_of_rooms = models.IntegerField(default=0)
    picture1 = models.ImageField(upload_to='images/accomodation', null=True, blank=True) 
    picture2 = models.ImageField(upload_to='images/accomodation', null=True, blank=True) 
    picture3 = models.ImageField(upload_to='images/accomodation', null=True, blank=True) 
    picture4 = models.ImageField(upload_to='images/accomodation', null=True, blank=True) 
    picture5 = models.ImageField(upload_to='images/accomodation', null=True, blank=True) 

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)


class HotelOrder(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='user')
    supplier = models.ForeignKey(Account, on_delete=models.CASCADE,null=True, blank=True,related_name='supplier')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=15,default='unpaid')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,default='')
    order_price = models.DecimalField(max_digits=50, decimal_places=2)
    hotel_shared_room_capacity = models.IntegerField(null=True, blank=True)
    order_travalers = models.CharField(max_length=2)
    hotel_order_start_date = models.DateField()
    hotel_order_end_date = models.DateField()




# class RoomCheckout(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     room_checkout = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)


class Apartment(models.Model):
    apartment_name = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    CHOICE_OF_APARTMENTS = (
        ('1', 'Studio'),
        ('2', 'F1'),
        ('3', 'F2'),
        ('4', 'F3'),
        ('5', 'F4'),
        ('6', 'villa'),
    )
    choice_of_apartment = models.CharField(max_length=256, choices=CHOICE_OF_APARTMENTS)
    capacity = models.PositiveIntegerField(validators=[MaxValueValidator(20)])
    WiFi_connection = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    availability = models.BooleanField(default=True)


class Car(models.Model):
    type = models.CharField(max_length=10, default='car')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    destination = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    PICK_UP_LOCATION = (
        ('1', 'Airport'),
        ('2', 'Hotel'),
        ('3', 'Agency'),
    )
    pick_up_location = models.CharField(max_length=256, choices=PICK_UP_LOCATION)
    pick_up_destination = models.CharField(max_length=256, default="")
    CAR_TYPES = (
        ('1', 'Coupe'),
        ('2', 'Sedan'),
        ('3', 'Van'),
    )
    car_types = models.CharField(max_length=256, choices=CAR_TYPES)
    mark = models.ForeignKey(to='adminPanel.CarMark', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    number_of_sits = models.SmallIntegerField()
    picture1 = models.ImageField(upload_to='images/cars', default='images/brand-2.jpg')
    picture2 = models.ImageField(upload_to='images/cars', default='images/brand-2.jpg')
    permission = models.BooleanField(default=False)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return str(self.mark)


class AccommodationReview(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.SmallIntegerField(default=5)
    permition = models.BooleanField(default=False)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Accommodation Reviews"


class CarReview(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.SmallIntegerField(default=5)
    permition = models.BooleanField(default=False)
    notification = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Car Reviews"


class AccommodationOrder(models.Model):
    name = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    accomodation_order_start_date = models.DateField()
    accomodation_order_end_date = models.DateField()


class AccomodationCheckout(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    accomodation_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)


class OrderCar(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_order_start_date = models.DateField()
    car_order_end_date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')

