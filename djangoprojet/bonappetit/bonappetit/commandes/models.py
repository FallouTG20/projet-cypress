from django.db import models
from django.conf import settings
from menus.models import Menu

class Notification(models.Model):
    """
    Modèle pour les notifications des commandes
    """
    commande = models.ForeignKey('Commande', on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)
    est_gestionnaire = models.BooleanField(default=False)  # True si c'est une notification pour le gestionnaire

    def __str__(self):
        return f"Notification pour {'Gestionnaire' if self.est_gestionnaire else 'Client'} - {self.commande} - {self.date_creation}"

class Commande(models.Model):
    """
    Modèle pour les commandes des clients
    """
    class Statut(models.TextChoices):
        EN_ATTENTE = 'EN_ATTENTE', 'En attente'
        EN_PREPARATION = 'EN_PREPARATION', 'En préparation'
        PRETE = 'PRETE', 'Prête'
        LIVREE = 'RECUPEREE', 'Récupérée'
        ANNULEE = 'ANNULEE', 'Annulée'

    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commandes')
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )
    telephone = models.CharField(max_length=15)
    notes = models.TextField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Commande #{self.id} - {self.client.username}"

    def save(self, *args, **kwargs):
        statut_initial = None
        if self.pk:
            statut_initial = Commande.objects.get(pk=self.pk).statut
        super().save(*args, **kwargs)
        if statut_initial and statut_initial != self.statut and self.statut == 'PRETE':
            from .models import Notification
            Notification.objects.create(
                commande=self,
                message="Votre commande est prête ! Vous pouvez venir la récupérer."
            )

class LigneCommande(models.Model):
    """
    Modèle pour les lignes de commande (items individuels dans une commande)
    """
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    sous_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.sous_total = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)
        # Mettre à jour le total de la commande
        self.commande.total = sum(ligne.sous_total for ligne in self.commande.lignes.all())
        self.commande.save()

    def __str__(self):
        return f"{self.quantite}x {self.menu.nom}"
