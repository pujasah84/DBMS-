from django import forms
from django.contrib.auth.models import User
from .models import Customer, Account



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user == None or not user.check_password(password):
            raise forms.ValidationError("Invalid username or password")
        return self.cleaned_data


class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['account']

class accountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"