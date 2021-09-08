from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
# from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse

def sign_up(request):
    print("hellooooooooooooooooo")
    if request.is_ajax():
        form = RegistrationForm(request.POST, request.FILES)
        date = request.POST.get('date')
        print(date, "===================")
        if form.is_valid():
            print("valiiiiiiiiiiiiiiiid")
            data = form.save(commit=False)
            if request.POST.get('user_type')=="customer":
                data.is_supplier = False
                data.date_of_birth = date
                data.save()
                new_user = authenticate(email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1'],)
                login(request, new_user)
                return redirect('homepage:homepage')
            elif request.POST.get('user_type')=="supplier":
                print("ara aq movedi")
                data.is_supplier = True
                data.date_of_birth = date
                data.is_active = False
                data.save()
                # messages.errors(request, 'your request has been sent to admin')
                return redirect('homepage:homepage')
        else:
            print(form.errors)
            # messages.error(request, form.errors)
            i=JsonResponse({'error':form.errors})
            i.status_code=403
            return i


def login_page(request):
    form = LoginForm()
    print("fuuchbuuuuuuuuuuuu")
    if request.is_ajax():
        form = LoginForm(request.POST or None)
        try:
            print("fuuchbuuuuuuuuuuuu")

            Account.objects.get(email=request.POST.get('email'))

            if form.is_valid():
                print("fuuchbuuuuuuuuuuuu")
                data = form.cleaned_data
                user = authenticate(email=str(data['email']), password=str(data['password']))
                login(request, user)
                

                if user.is_supplier:
                    # return redirect('userProfile:supplierItems')
                    return JsonResponse({'user':'supplier'})
                    
                elif user.is_superuser:
                    # return redirect('adminPanel:dashboard')
                    return JsonResponse({'user':'admin'})
                else:
                    # return redirect('userProfile:customerProfile', request.user.id)
                    return JsonResponse({'user':'customer'})
                messages.error(request, form.errors)
        except:
            messages.error(request, form.errors)
            

def login_redirect(request, email):
    user = Account.objects.get(email=email)
    if user.is_supplier:
        return redirect('userProfile:supplierItems')
    elif user.is_superuser:
        return redirect('adminPanel:dashboard')
    else:
        return redirect('userProfile:customerProfile', request.user.id)

            
def logout_page(request):
    logout(request)
    return redirect('homepage:homepage')