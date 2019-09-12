from django import forms
import clearbit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from DishChoser.keys import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2']

    def search_person(self, email):
        clearbit.key = clearbit_key
        person = clearbit.Person.find(email=str(email), stream=True)
        if person != None:
            print("Name: " + person['name']['fullName'])


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data

