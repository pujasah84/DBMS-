from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        print(self.cleaned_data)
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user == None or not user.check_password(password):
            raise forms.ValidationError("Invalid username or password")
        return self.cleaned_data