from django.urls import path
from . import views

urlpatterns = [
    path('panier/', views.panier, name='panier'),
    path('ajouter-au-panier/<int:menu_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('retirer-du-panier/<int:menu_id>/', views.retirer_du_panier, name='retirer_du_panier'),
    path('passer-commande/', views.passer_commande, name='passer_commande'),
    path('mes-commandes/', views.mes_commandes, name='mes_commandes'),
    path('commande/<int:commande_id>/', views.detail_commande, name='detail_commande'),
    path('commande/<int:commande_id>/annuler/', views.annuler_commande, name='annuler_commande'),
    path('gestion-commandes/', views.gestion_commandes, name='gestion_commandes'),
    path('commande/<int:commande_id>/modifier-statut/', views.modifier_statut_commande, name='modifier_statut_commande'),
    path('notifications/<int:notification_id>/marquer-lue/', views.marquer_notification_lue, name='marquer_notification_lue'),
    path('notifications/<int:notification_id>/supprimer/', views.supprimer_notification, name='supprimer_notification'),
    path('notifications/nombre-non-lues/', views.nombre_notifications_non_lues, name='nombre_notifications_non_lues'),
    path('notifications/', views.notifications, name='notifications'),
] 