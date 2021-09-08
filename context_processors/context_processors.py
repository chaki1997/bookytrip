from adminPanel.models import FooterDescription
from registration.forms import RegistrationForm, LoginForm
from components.models import About
def get_footer(request):
    footer = FooterDescription.objects.get(id=1)
    return {
        'footer': footer
    }


def get_registration_form(request):

    registration_form = RegistrationForm()

    return {
        'registration_form':registration_form
    }


def get_login_form(request):

    login_form = LoginForm()

    return {
        'login_form': login_form
    }

