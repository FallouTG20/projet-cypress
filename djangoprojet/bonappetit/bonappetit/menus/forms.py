from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nom', 'description', 'prix', 'image', 'categorie', 'disponible']
