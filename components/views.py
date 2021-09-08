from django.shortcuts import render,redirect
from adminPanel.models import FooterDescription
from .forms import FaqForm, ContactForm
from .models import Faq, WhyUs, About, Vendor
from adminPanel.models import PrivacyPolicy, TermsAndConditions


def faq_view(request):

	form = FaqForm()
	faq = Faq.objects.all()

	if request.user.is_authenticated:
		if request.method=="POST":
			form = FaqForm(request.POST or None)
			if form.is_valid():
				data = form.save(commit=False)
				data.user = request.user
				data.save()

				return redirect("components:faq")
		else:
			form = FaqForm()

	context = {

		'faqs':faq,
		'form':form,
	}
	return render(request,'components/faq.html',context)


def about_view(request):

	why_us        = WhyUs.objects.all()
	about_content = About.objects.all()
	vendors       = Vendor.objects.all()

	context = {
		'why_us':why_us,
		'about_content':about_content,
		'vendors':vendors,
	}

	return render(request,"components/about.html",context)


def contact_view(request):

	form = ContactForm()

	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('components:contact')

	context = {
		'form':form,
	}

	return render(request, "components/contact.html",context)


def privacy_policy(request):

	privacy_policy = PrivacyPolicy.objects.get(id=1)

	context = {
		'privacy_policy':privacy_policy,
	}

	return render(request, 'components/privacy_policy.html', context)


def terms_and_conditions(request):

	term = TermsAndConditions.objects.get(id=1)

	context = {
		'term':term,
	}

	return render(request, 'components/terms_and_conditions.html', context)
