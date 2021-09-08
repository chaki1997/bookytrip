from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password*'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmation Password*'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email*'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name*'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname*'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'', 'id': 'phone'}))
    picture = forms.CharField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Account
        fields = ('email', 'name','surname','phone', 'picture')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):


    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone', 'date_of_birth', 'picture', 'access_adminpanel', 'access_users',
                 'access_components', 'access_perosnaltour', 'access_themedtour')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Passowrd'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Passowrd'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datepickers','type':'text', 'placeholder': 'dd-mm-yyyy', 'autocomplete':'off'}))
    picture = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone', 'date_of_birth', 'picture', 'is_supplier', 'is_active')

    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datepickers','type':'text', 'placeholder': 'dd-mm-yyyy', 'autocomplete':'off'}))
    picture = forms.FileField(widget=forms.ClearableFileInput())
    # is_supplier = forms.BooleanField(label = 'is supplier?', widget=forms.CheckboxInput(attrs={}))
    # is_active = forms.BooleanField(label = 'Permission', widget=forms.CheckboxInput(attrs={}))


    
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class AdminChangeForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'name', 'surname', 'phone', 'date_of_birth', 'picture', 'access_adminpanel', 'access_users',
                 'access_components', 'access_perosnaltour', 'access_themedtour')

    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datepickers','type':'text', 'placeholder': 'dd-mm-yyyy', 'autocomplete':'off'}))
    picture = forms.FileField(widget=forms.ClearableFileInput())

    
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control",
                                                            'id': 'email',
                                                            "placeholder": "Email",
                                                            "type": "email",
                                                            "name": "email"}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",
                                                                'id': 'password',
                                                                "placeholder": "Password",
                                                                "type": "password",
                                                                "name": "password"}))

