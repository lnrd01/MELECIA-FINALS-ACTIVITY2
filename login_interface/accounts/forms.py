from django import forms
from django.contrib.auth.models import User


INPUT_STYLE = 'w-full bg-gray-300 text-gray-800 rounded-xl px-5 py-4'

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username/Email',
        widget=forms.TextInput(attrs={'class': INPUT_STYLE, 'placeholder': 'Username/Email'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_STYLE, 'placeholder': 'Enter your password'}),
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match')
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # hashes the password
        if commit:
            user.save()
        return user