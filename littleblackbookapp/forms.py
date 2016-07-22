from django import forms

from .models import Professional, Company

class ProfessionalForm(forms.ModelForm):
    """
    renames a variety of model columns for user interaction
    """
    phone2 = forms.CharField(label="Phone 2")
    email2 = forms.EmailField(label="E-mail 2")
    website2 = forms.URLField(label="Website 2")
    goals = forms.CharField(label="What are this professionals goals or needs?  What opportunities exist to suggest win-win situations?")
    # meetupid = forms.CharField(label='Meetup ID')
    # eventshostedname = forms.CharField(label='Events Hosted')
    # ohbcontributions = forms.IntegerField(label='Open Heart Brigade Participation')
    # ohb = forms.NullBooleanField(label="Open Heart Brigade")
    # launchteam = forms.NullBooleanField(label="Launch Team")
    # launchteamcontributions = forms.IntegerField(label="Launch Team Contributions")
    # fbgroupmember = forms.NullBooleanField(label="Facebook Group Member")
    # fbpagelink = forms.URLField(label="Facebook Page Link")
    # donationtotalammount = forms.IntegerField(label="Donation Ammount")

    class Meta:
        model = Professional
        fields = ('name', 'email', 'phone', 'website', 'level', 'neighborhood', 'goals', 'address', 'phone2', 'email2', 'website2', 'company',
        )

class CompanyForm(forms.ModelForm):
    """
    provides user input for Companies
    """
    class Meta:
        model = Company
        fields = ('name', 'email', 'phone', 'website', 'address',
        )
