from django.db import models

# Create your models here.

class Menu(models.Model):
    CATEGORIE_CHOICES = [
        ('entree', 'Entrée'),
        ('plat', 'Plat'),
        ('dessert', 'Dessert'),
        ('boisson', 'Boisson'),
        ('fast-food', 'Fast-Food'),
        ('snack', 'Snack'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menus/', null=True, blank=True)
    disponible = models.BooleanField(default=True)
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)

    def __str__(self):
        return self.nom

