from django import forms
from .models import Faq, Contact, WhyUs, About, Vendor


class FaqForm(forms.ModelForm):
	class Meta:
		model = Faq
		fields = ('question_type', 'question')

	question_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'selectpicker form-control',}),
                                                 choices = ([('1','Pre-Sale Questions'), ('2','Other Types')]))
	question = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id':'Question'}))


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
														'placeholder':"Name",}))

	surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
															'placeholder':"Surname",}))

	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
													     'placeholder':'Email'}))

	text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
														   'placeholder':'Message'}))

class WhyUsForm(forms.ModelForm):
    class Meta:
        model = WhyUs
        fields = '__all__'

    image  = forms.FileField(widget=forms.ClearableFileInput())
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    text   = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


    top_title  = forms.CharField(widget=forms.TextInput(attrs={'class':'footer_textarea form-control', 'id': 'editor'}))
    top_text   = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text'}))
    cover_file = forms.FileField(widget=forms.ClearableFileInput())
    title      = forms.CharField(widget=forms.TextInput(attrs={'class':'footer_textarea form-control', 'id': 'editor'}))
    image1     = forms.FileField(widget=forms.ClearableFileInput())
    text1      = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text'}))
    image2     = forms.FileField(widget=forms.ClearableFileInput())
    text2      = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text'}))
    image3     = forms.FileField(widget=forms.ClearableFileInput())
    text3      = forms.CharField(widget=forms.Textarea(attrs={'class':'footer_textarea form-control', 'id': 'interesting_text'}))


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('logo',)

    logo = forms.FileField(widget=forms.ClearableFileInput())