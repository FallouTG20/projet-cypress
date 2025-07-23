from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    """
    Formulaire d'inscription personnalisé
    """
    first_name = forms.CharField(label='Prénom', max_length=30, required=True)
    last_name = forms.CharField(label='Nom', max_length=30, required=True)
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telephone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.telephone = self.cleaned_data['telephone']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    """
    Formulaire de mise à jour du profil utilisateur
    """
    first_name = forms.CharField(label='Prénom', max_length=30, required=True)
    last_name = forms.CharField(label='Nom', max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telephone'] 