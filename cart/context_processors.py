from .cart import Cart

def cart(request):
    print(Cart(request).cart)
    return {'cart':Cart(request)}



