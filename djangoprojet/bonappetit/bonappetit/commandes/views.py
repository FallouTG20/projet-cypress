from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Commande, LigneCommande, Notification
from menus.models import Menu
import json

@login_required
def panier(request):
    """
    Vue pour afficher le panier de l'utilisateur
    """
    panier = request.session.get('panier', {})
    total = 0
    menus_panier = {}

    for menu_id, details in panier.items():
        menu = Menu.objects.get(id=menu_id)
        sous_total = details['quantite'] * details['prix']
        menus_panier[menu_id] = {
            'menu': menu,
            'quantite': details['quantite'],
            'prix': details['prix'],
            'sous_total': sous_total
        }
        total += sous_total

    context = {
        'menus_panier': menus_panier,
        'total': total
    }
    return render(request, 'commandes/panier.html', context)

@login_required
def ajouter_au_panier(request, menu_id):
    """
    Vue pour ajouter un menu au panier
    """
    menu = get_object_or_404(Menu, id=menu_id)
    panier = request.session.get('panier', {})
    
    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        # Gestion de la mise à jour de quantité via AJAX
        data = json.loads(request.body)
        nouvelle_quantite = data.get('quantity', 1)
        
        if nouvelle_quantite > 0:
            panier[str(menu_id)] = {
                'quantite': nouvelle_quantite,
                'prix': float(menu.prix),
                'nom': menu.nom
            }
        else:
            # Si la quantité est 0 ou négative, retirer du panier
            if str(menu_id) in panier:
                del panier[str(menu_id)]
    else:
        # Ajout normal au panier
        if str(menu_id) in panier:
            panier[str(menu_id)]['quantite'] += 1
        else:
            panier[str(menu_id)] = {
                'quantite': 1,
                'prix': float(menu.prix),
                'nom': menu.nom
            }
    
    request.session['panier'] = panier
    messages.success(request, f'{menu.nom} a été ajouté au panier.')
    
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({'success': True})
    return redirect('panier')

@login_required
def passer_commande(request):
    if request.method == 'POST':
        panier = request.session.get('panier', {})
        if not panier:
            messages.error(request, 'Votre panier est vide')
            return redirect('panier')

        # Créer la commande
        commande = Commande.objects.create(
            client=request.user,
            statut='EN_ATTENTE',
            total=0  # Sera mis à jour par les lignes de commande
        )

        total_commande = 0
        for menu_id, details in panier.items():
            menu = get_object_or_404(Menu, id=menu_id)
            quantite = details['quantite']
            prix = details['prix']
            sous_total = prix * quantite
            total_commande += sous_total

            LigneCommande.objects.create(
                commande=commande,
                menu=menu,
                quantite=quantite,
                prix_unitaire=prix
            )

        commande.total = total_commande
        commande.save()

        # Vider le panier
        request.session['panier'] = {}
        messages.success(request, 'Votre commande a été enregistrée avec succès')
        return redirect('mes_commandes')

    # GET request - afficher le formulaire de confirmation
    panier = request.session.get('panier', {})
    if not panier:
        messages.error(request, 'Votre panier est vide')
        return redirect('panier')

    total = 0
    menus_panier = {}
    for menu_id, details in panier.items():
        menu = get_object_or_404(Menu, id=menu_id)
        sous_total = details['quantite'] * details['prix']
        menus_panier[menu_id] = {
            'menu': menu,
            'quantite': details['quantite'],
            'prix': details['prix'],
            'sous_total': sous_total
        }
        total += sous_total

    context = {
        'menus_panier': menus_panier,
        'total': total
    }
    return render(request, 'commandes/passer_commande.html', context)

@login_required
def mes_commandes(request):
    """
    Vue pour afficher les commandes de l'utilisateur
    """
    commandes = Commande.objects.filter(client=request.user).order_by('-date_commande')
    return render(request, 'commandes/mes_commandes.html', {'commandes': commandes})

@login_required
def detail_commande(request, commande_id):
    """
    Vue pour afficher les détails d'une commande
    """
    commande = get_object_or_404(Commande, id=commande_id, client=request.user)
    return render(request, 'commandes/detail_commande.html', {'commande': commande})

@login_required
def annuler_commande(request, commande_id):
    """
    Vue pour annuler une commande
    """
    commande = get_object_or_404(Commande, id=commande_id, client=request.user)
    if commande.statut == Commande.Statut.EN_ATTENTE:
        commande.statut = Commande.Statut.ANNULEE
        commande.save()
        messages.success(request, 'Votre commande a été annulée.')
    else:
        messages.error(request, 'Cette commande ne peut plus être annulée.')
    return redirect('mes_commandes')

@login_required
def retirer_du_panier(request, menu_id):
    """
    Vue pour retirer un menu du panier
    """
    panier = request.session.get('panier', {})
    if str(menu_id) in panier:
        del panier[str(menu_id)]
        request.session['panier'] = panier
        messages.success(request, 'Le menu a été retiré du panier.')
    return redirect('panier')

# Vues pour le gestionnaire
@login_required
def gestion_commandes(request):
    """
    Vue pour le gestionnaire pour voir toutes les commandes
    """
    if not request.user.is_gestionnaire():
        messages.error(request, 'Accès non autorisé.')
        return redirect('home')
    
    commandes = Commande.objects.all().order_by('-date_commande')
    return render(request, 'commandes/gestion_commandes.html', {'commandes': commandes})

@login_required
def modifier_statut_commande(request, commande_id):
    """
    Vue pour le gestionnaire pour modifier le statut d'une commande
    """
    if not request.user.is_gestionnaire():
        return JsonResponse({'error': 'Accès non autorisé'}, status=403)
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    commande = get_object_or_404(Commande, id=commande_id)
    try:
        data = json.loads(request.body)
        nouveau_statut = data.get('statut')
    except Exception:
        return JsonResponse({'error': 'Requête invalide'}, status=400)
    if nouveau_statut in dict(Commande.Statut.choices):
        commande.statut = nouveau_statut
        commande.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Statut invalide'}, status=400)

@login_required
def marquer_notification_lue(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, commande__client=request.user)
    notification.lu = True
    notification.save()
    return redirect('notifications')

@login_required
def supprimer_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, commande__client=request.user)
    notification.delete()
    return redirect('notifications')

@login_required
def nombre_notifications_non_lues(request):
    nombre = Notification.objects.filter(commande__client=request.user, lu=False).count()
    return JsonResponse({'nombre': nombre})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(commande__client=request.user).order_by('-date_creation')
    return render(request, 'commandes/notifications.html', {'notifications': notifications})
