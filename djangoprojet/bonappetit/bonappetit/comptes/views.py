from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm
from .models import User
from django.db.models import Count, Sum
from django.db.models.functions import ExtractWeekDay
from commandes.models import Commande, LigneCommande
from menus.models import Menu
from django.utils import timezone
from datetime import timedelta

def register(request):
    """
    Vue pour l'inscription des utilisateurs
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Votre compte a été créé avec succès!')
            return redirect('accueil')
    else:
        form = UserRegistrationForm()
    return render(request, 'comptes/register.html', {'form': form})

@login_required
def profile(request):
    """
    Vue pour afficher et modifier le profil utilisateur
    """
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'comptes/profile.html', {'form': form})

@login_required
def dashboard(request):
    """
    Vue pour le tableau de bord utilisateur
    """
    if request.user.is_gestionnaire():
        return render(request, 'comptes/gestionnaire_dashboard.html')
    return render(request, 'comptes/client_dashboard.html')

@login_required
def statistiques(request):
    if not request.user.is_gestionnaire:
        return redirect('accueil')
    
    # Statistiques par menu
    menu_stats = LigneCommande.objects.values('menu__nom').annotate(
        total=Count('id')
    ).order_by('-total')
    
    menu_labels = [stat['menu__nom'] for stat in menu_stats]
    menu_data = [stat['total'] for stat in menu_stats]
    
    # Statistiques par jour de la semaine
    day_stats = Commande.objects.annotate(
        jour=ExtractWeekDay('date_commande')
    ).values('jour').annotate(
        total=Count('id')
    ).order_by('jour')
    
    # Initialiser un tableau avec des zéros pour chaque jour
    day_data = [0] * 7
    for stat in day_stats:
        # Convertir le jour (1-7) en index (0-6)
        day_data[stat['jour'] - 1] = stat['total']
    
    # Top 10 des utilisateurs
    top_users = Commande.objects.values(
        'client__username',
        'client__id'
    ).annotate(
        total_orders=Count('id')
    ).order_by('-total_orders')[:10]
    
    # Statistiques supplémentaires
    total_commandes = Commande.objects.count()
    commandes_aujourdhui = Commande.objects.filter(
        date_commande__date=timezone.now().date()
    ).count()
    
    commandes_semaine = Commande.objects.filter(
        date_commande__gte=timezone.now().date() - timedelta(days=7)
    ).count()
    
    # Chiffre d'affaires total
    chiffre_affaires = Commande.objects.aggregate(
        total=Sum('total')
    )['total'] or 0
    
    context = {
        'menu_labels': menu_labels,
        'menu_data': menu_data,
        'day_data': day_data,
        'top_users': top_users,
        'total_commandes': total_commandes,
        'commandes_aujourdhui': commandes_aujourdhui,
        'commandes_semaine': commandes_semaine,
        'chiffre_affaires': chiffre_affaires,
    }
    
    return render(request, 'comptes/statistiques.html', context)

def profile_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'comptes/profile_detail.html', {'user_detail': user})
