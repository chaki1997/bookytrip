from django.shortcuts import render

# Create your views here.

def supplier_payment(request):

    return render(request, 'supplier/my_payments.html', {})