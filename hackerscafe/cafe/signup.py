from django import forms
from django.core import validators
from cafe.models import signupModel

class signupForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    email      = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter email again")
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        first_name     = all_clean_data['first_name']
        last_name      = all_clean_data['last_name']
        email          = all_clean_data['email']
        verify_email   = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError(("[-] Emails do not match!",))
        return

    class Meta():
        model  = signupModel
        fields = '__all__'



