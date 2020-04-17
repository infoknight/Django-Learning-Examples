from django import forms
from django.contrib.auth.models import User
from django.core import validators
from signup.models import UserProfileInfoModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site', 'profile_pic')


'''
class newregForm(forms.ModelForm):          #Need to add Input Validation
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again")
    password = forms.CharField(widget = forms.PasswordInput())
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails do not match!")
        return
    
    class Meta():
        model = regModel
        fields = ('first_name', 'last_name', 'email', 'password')
'''


'''
class UserProfileInfoForms(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site', 'profile_pic')
'''




'''
class regForm(forms.Form):          #Need to add Input Validation
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again")
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email == vmail:
            raise forms.ValidationError("Emails do not match!")
        return
'''
