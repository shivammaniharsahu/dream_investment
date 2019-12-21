from django import forms
from .models import Students


class EmpForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['full_name', 'email', 'mobile_number', 'message']
     #   full_name = forms.TextInput(attrs={'id': 'name',  'class' : 'input100'})
     #   mobile_number = forms.TextInput(attrs={'id': 'phone',  'class' : 'input100'})
     #   email = forms.EmailInput(attrs={'id': 'email',  'class' : 'input100'})
     # message = forms.TextInput(attrs={'id': 'message',  'class' : 'input100'})