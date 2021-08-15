from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
        def __init__(self, *args, **kwargs):
            super(UserRegistrationForm, self).__init__(*args, **kwargs)
            for name, field in fields.items():
                field.args.attr.update({'input': 'form-control'})

    def clean_password(self):
        created = self.cleaned_data
        if created['password2'] != created['password']:
            raise ValidationError('password do not match')
