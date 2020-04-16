from django import forms
from django.core import validators
from signup.models import regModel

class newregForm(forms.ModelForm):          #Need to add Input Validation
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again")
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
        fields = '__all__'

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
