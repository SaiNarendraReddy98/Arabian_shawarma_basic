from django import forms
from app.models import *

#creating forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':''}



class SigninDataForm(forms.ModelForm):
    class Meta:
        model = SigninData
        fields = '__all__'


        
