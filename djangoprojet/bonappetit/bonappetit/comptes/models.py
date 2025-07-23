from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Modèle d'utilisateur personnalisé avec deux rôles : client et gestionnaire
    """
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', _('Client')
        GESTIONNAIRE = 'GESTIONNAIRE', _('Gestionnaire')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
    )
    telephone = models.CharField(max_length=15, blank=True)

    def is_client(self):
        return self.role == self.Role.CLIENT

    def is_gestionnaire(self):
        return self.role == self.Role.GESTIONNAIRE
