from django.shortcuts import render
from .models import Menu
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MenuForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def accueil(request):
    return render(request, 'menus/accueil.html')

def liste_menus(request):
    # Récupérer la catégorie sélectionnée depuis les paramètres GET
    categorie = request.GET.get('categorie')
    
    # Filtrer les menus selon la catégorie si elle est spécifiée
    if categorie:
        menus = Menu.objects.filter(categorie=categorie)
    else:
        menus = Menu.objects.all()
    
    # Récupérer toutes les catégories pour le filtre
    categories = dict(Menu.CATEGORIE_CHOICES)
    
    context = {
        'menus': menus,
        'categories': categories,
        'categorie_actuelle': categorie
    }
    return render(request, 'menus/liste_menus.html', context)


@login_required
def gestion_menus(request):
    if not request.user.is_gestionnaire():
        messages.error(request, "Accès réservé au gestionnaire.")
        return redirect('accueil')
    menus = Menu.objects.all()
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu ajouté avec succès.")
            return redirect('gestion_menus')
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez corriger les champs.")
    else:
        form = MenuForm()
    return render(request, 'menus/gestion.html', {'form': form, 'menus': menus})

def modifier_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    form = MenuForm(request.POST or None, request.FILES or None, instance=menu)

    if form.is_valid():
        form.save()
        return redirect('gestion_menus')

    return render(request, 'menus/modifier.html', {'form': form})

def supprimer_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menu.delete()
    return redirect('gestion_menus')

@login_required
def ajouter_au_panier(request, menu_id):
    if request.method == 'POST':
        menu = get_object_or_404(Menu, id=menu_id)
        quantite = int(request.POST.get('quantite', 1))
        
        # Récupérer ou créer le panier dans la session
        panier = request.session.get('panier', {})
        
        # Ajouter ou mettre à jour la quantité du menu dans le panier
        if str(menu_id) in panier:
            panier[str(menu_id)]['quantite'] += quantite
        else:
            panier[str(menu_id)] = {
                'nom': menu.nom,
                'prix': float(menu.prix),
                'quantite': quantite
            }
        
        # Sauvegarder le panier dans la session
        request.session['panier'] = panier
        messages.success(request, f'{menu.nom} a été ajouté à votre panier.')
        
        # Rediriger vers la page précédente ou la liste des menus
        return redirect(request.META.get('HTTP_REFERER', 'liste_menus'))
    
    return redirect('liste_menus')

@login_required
def modifier_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le menu a été modifié avec succès.')
            return redirect('gestion_menus')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menus/modifier_menu.html', {'form': form, 'menu': menu})

@login_required
def supprimer_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == 'POST':
        menu.delete()
        messages.success(request, 'Le menu a été supprimé avec succès.')
        return redirect('gestion_menus')
    return render(request, 'menus/supprimer_menu.html', {'menu': menu})


