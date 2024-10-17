# 1st form - register or create account
# 2nd form - login

# import Record model
from .models import Record

# user creation by model's attributes
from django.contrib.auth.forms import UserCreationForm

# authentication form
from django.contrib.auth.forms import AuthenticationForm

# user model
from django.contrib.auth.forms import User

# form elements
from django import forms

# widgets 
from django.forms.widgets import PasswordInput, TextInput



#---------------------------------------------------------------

# - Register/Create a User
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User

        # password1 for setting password, password2 - confirming password
        fields = ['username', 'password1', 'password2']


# - Login a User
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())


# - Create a Record
class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['klijent','tip_stranke', 'email', 'telefon', 'uredjaj', 'opis_zahteva']


# - Update a Record
class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['klijent','tip_stranke', 'email', 'telefon', 'uredjaj', 'opis_zahteva']