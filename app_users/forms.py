from django import forms
from .models import Users


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'date_born']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
