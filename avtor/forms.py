from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Введите адрес электронной почты.',
            'invalid': 'Введите корректный адрес электронной почты.',
        }
    )
    username = forms.CharField(
        max_length=150,
        error_messages={
            'required': 'Введите имя пользователя.',
            'max_length': 'Имя пользователя не может превышать 150 символов.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
