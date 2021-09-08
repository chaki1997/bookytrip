from django.conf import settings
from personalTour.models import Hotel,Car
from decimal import Decimal

class Cart(object):

    def __init__(self,request):
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        cart_calcs = self.session.get(settings.CART_SESSION_CALCS)
        cart_car = self.session.get(settings.CART_SESSION_CAR)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        if not cart_calcs:
            cart_calcs = self.session[settings.CART_SESSION_CALCS] = {}
        self.cart_calcs = cart_calcs
        #if not cart_car:
        #    cart_car = self.session[settings.CART_SESSION_CAR] = {}
        #self.cart_car = cart_car

    def add(self,product,start_date,end_date,hotel_id,car_id,dinamic_capacity,override_quantity=False):
        product_id = str(product.id)
        #self.prod_id=product_id
        print(product.type)
        if product.type == 'hotel':
            if product_id not in self.cart:
                if dinamic_capacity:
                    capacity=str(dinamic_capacity)
                else:
                    capacity = str(product.capacity)


                self.cart[product_id]={'type':product.type,'quantity':1,'price':str(product.price),'start_date':start_date,'end_date':end_date,'hotel_id':hotel_id,'room_type':str(product.room_type),
                                       'capacity': capacity}
            else:
                self.cart[product_id]['quantity']+=1
                print('quantity',self.cart[product_id]['quantity'])
            if  bool(self.cart_calcs):
                self.cart_calcs['total_order_price_hotel']=self.cart_calcs['total_order_price_hotel']+float(product.price)
            else:
                self.cart_calcs['total_order_price_hotel']=float(product.price)

            #if override_quantity:
            #    self.cart[product_id]['quantity'] = quantity
            #else:
            #    self.cart[product_id]['quantity'] += quantity
            self.save()
        else:
            self.cart[product_id+'_car'] = {'type':product.type,'price':float(product.price),'quantity':1,
                                            'start_date':start_date,
                                            'end_date':end_date,
                                            'car_id':product.id}
            print('-----------------------------car-----',start_date,end_date)
            if  bool(self.cart_calcs):
                print('total_price_1')
                if 'total_order_price_car' in self.cart_calcs.keys():
                    self.cart_calcs['total_order_price_car']=self.cart_calcs['total_order_price_car']+float(product.price)
                else:
                    self.cart_calcs['total_order_price_car'] = float(product.price)

            else:
                self.cart_calcs['total_order_price_car']=float(product.price)
                print('total_price_2')
            self.save()


        #if override_quantity:
        #    self.cart[product_id]['quantity'] = quantity
        #else:
        #    self.cart[product_id]['quantity'] += quantity
        #self.save()

    def save(self):
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            #for item in self.cart.values():
                # total_order_price += product.price
           #     item['total_order_price'] = str(float(item['total_order_price'])-float(product.price))
            self.cart_calcs['total_order_price'] = self.cart_calcs['total_order_price']-float(product.price)
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        #product_ids = self.cart.keys()
        product_ids=[]
        car_ids = []
        for i in self.cart.keys():
            if not 'car' in i:
                product_ids.append(i)
            else:

                car_ids.append(i.split('_')[0])
        products = Hotel.objects.filter(id__in=product_ids)
        cars = Car.objects.filter(id__in=car_ids)

        cart = self.cart.copy()

        order_price=0

        for product in products:
            cart[str(product.id)]['product'] = product

        for car in cars:
            cart[str(car.id)+'_car']['product'] = car

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price'] = item['price']*item['quantity']

            #order_price+=item['price']
            print('---------item-----------',item)
            yield item

        #for item in cart.values():
         #   item['order_price'] = order_price

    #def __str__(self):
    #    return str(self.cart)
'''
class Cart(object):

    def __init__(self,request):
        self.session=request.session

        cart_car = self.session.get(settings.CART_SESSION_CAR)
        if not cart_car:
            cart_car = self.session[settings.CART_SESSION_ID] = {}
        self.cart_car = cart_car
'''