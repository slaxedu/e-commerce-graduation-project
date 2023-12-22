from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms 
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm, forms.Form):
    phone_number = PhoneNumberField(region="EG")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number') 



class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email','phone_number' , 'password1', 'password2')
    phone_number = PhoneNumberField(region="EG",
        widget=PhoneNumberPrefixWidget(
            country_choices=[
                ("EG", "Egypt"),
                ("KSA", "Sudia Ariaba"),
            ],
            attrs={'class':'form-control',
                    'placeholder': 'Your Phone'}
            ), 
        
    )
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': 'form-control',
    }),)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': 'form-control',
    }))
    # phone_number = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Your Phone',
    #     'class' : 'form-control',
    # }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'form-control',
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / phone', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email or Phone'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Password'
    }))
    class Meta:
        model = CustomUser
        fields = ('username', 'password')