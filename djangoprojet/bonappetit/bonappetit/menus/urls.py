from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('menus/', views.liste_menus, name='liste_menus'),
    path('gestion/', views.gestion_menus, name='gestion_menus'),
    path('modifier/<int:menu_id>/', views.modifier_menu, name='modifier_menu'),
    path('supprimer/<int:menu_id>/', views.supprimer_menu, name='supprimer_menu'),
    path('ajouter-au-panier/<int:menu_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
]

