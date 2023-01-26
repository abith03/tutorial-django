from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django import forms
from Mymedicals.models import medicine


class medicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ["name","type","price","Mfg_date","Exp_date"]
        


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']