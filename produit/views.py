# coding=utf-8
import json
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import redirect
from messenger.models import Message
from website.decorators import ajax_required
from .models import Boutique, Produit, wish
from .forms import BoutiqueForm, SignUpForm, ProduitForm, CommercantForm, WishListForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
import logging
logr = logging.getLogger(__name__)
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class ProduitUpdate(UpdateView):
    model = Produit
    fields = ['prix', 'title', 'categorie','genrt' ,'descreption','tags' , 'type', 'etat', 'categorie','genre', 'logo', 'image1', 'image2',
              'image3']
    success_url = reverse_lazy('boutique:index' )
def group_based_upload_to(instance, filename):
    return "image/media/{}/{}".format(instance.boutique.name, filename)

def detail(request, boutique_id):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        user = request.user
        boutique = get_object_or_404(Boutique, pk=boutique_id)
        return render(request, 'produit/detail_boutique.html', {'boutique': boutique, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        boutiques = Boutique.objects.filter(user=request.user)
        produit_results = Produit.objects.all()
        query = request.GET.get("q")
        if query:
            boutiques = boutiques.filter(
                Q(name__icontains=query)).distinct()

            return render(request, 'produit/produits_all.html', {
                'boutiques': boutiques,
                'produits': produit_results,
            })
        else:
            return render(request, 'produit/index.html', {'boutiques': boutiques})


def create_boutique(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        form = BoutiqueForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            boutique = form.save(commit=False)
            boutique.user = request.user
            boutique.logo = request.FILES['logo']
            file_type = boutique.logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'produit/cree_boutique.html', context)
            boutique.save()
            return render(request, 'produit/detail_boutique.html', {'boutique': boutique})
        context = {
            "form": form,
        }
        return render(request, 'produit/cree_boutique.html', context)

def create_user(request):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        form = CommercantForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            boutique = form.save(commit=False)
            boutique.user = request.user
            print(boutique.user)
            boutique.save()
            return redirect ('/boutique/create_boutique')
        context = {
            "form": form,
        }
        return render(request, 'produit/commercant.html', context)

def delete_boutique(request, boutique_id):
    boutique = Boutique.objects.get(pk=boutique_id)
    boutique.delete()
    boutiques = Boutique.objects.filter(user=request.user)
    return render(request, 'produit/index.html', {'boutique': boutiques})


@ajax_required
def produit(request, filter_by):
        try:
            produit_ids = []
            for boutique in Boutique.objects.filter(user=request.user):
                for produit in boutique.produit_set.all():
                    produit_ids.append(produit.pk)
            users_produits = Produit.objects.filter(pk__in=produit_ids)
            if filter_by == 'favorites':
                users_produits = users_produits.filter(is_favorite=True)
        except Boutique.DoesNotExist:
            users_produits = []
        return render(request, 'produit/produits_all.html', {
            'produit_list': users_produits,
            'filter_by': filter_by,

        })

def produit_copy(request,produit_id):
    produit = get_object_or_404(Produit,pk=produit_id)
    produit.id = None
    produit.save()
    return render(request,'produit/index.html')


def create_produit(request, boutique_id):
    form = ProduitForm(request.POST or None, request.FILES or None)
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    print(boutique.album_set)
    if form.is_valid():
        boutiques_produits = boutique.produit_set.all()
        for s in boutiques_produits:
            if s.title == form.cleaned_data.get("title"):
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'You already added that produit',
                }
                return render(request, 'produit/cree_produit.html', context)
        produit = form.save(commit=False)
        produit.boutique = boutique
        produit.user = request.user
        produit.save()
        return render(request, 'produit/detail_boutique.html', {'boutique': boutique})
    context = {
        'boutique': boutique,
        'form': form,
    }
    return render(request, 'produit/cree_produit.html', context)

def delete_produit(request, boutique_id, produit_id):
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    produit = Produit.objects.get(pk=produit_id)
    produit.delete()
    return render(request, 'produit/detail_boutique.html', {'boutique': boutique})




class DetailView(generic.DetailView):
    model = Produit
    template_name = 'produit/detail-produit.html'


def boutique_detail(request,boutique_id):
    boutique = Boutique.objects.get(pk=boutique_id)
    msg_parametre(request,boutique_id)
    return render(request, 'produit/boutique_detail.html', {'boutique': boutique})


def post_list(request):
    list_produit = Produit.objects.all()
    paginator = Paginator(list_produit,8)
    page = request.GET.get('page')
    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    return render(request, 'produit/descover.html',{'page':page, 'produits':produits,

        })

def post_list2(request):
    list_produit = Produit.objects.all()
    paginator = Paginator(list_produit,8)
    page = request.GET.get('page')
    user = request.user
    age = user.profile.age
    print(age)


    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)

        produits = Produit.objects.all()

    return render(request, 'produit/produits_all.html',{'page':page, 'produits':produits,'list' : list_produit,
                                                        'bijoux': list_produit.filter(categorie='bijoux').count(),
                                                        'bijoux1': list_produit.filter(
                                                            categorie='maison et ameublement').count(),
                                                        'bijoux2': list_produit.filter(categorie='vetements').count(),
                                                        'bijoux3': list_produit.filter(
                                                            categorie='art et collections').count(),
                                                        'bijoux4': list_produit.filter(categorie='accessoires').count(),
                                                        'bijoux5': list_produit.filter(
                                                            categorie='sacs et bagages').count(),
                                                        'bijoux6': list_produit.filter(categorie='mariage').count()

                                                        })

def agefilter(request) :
    user = request.user
    age = Produit.objects.filter(profile__age = user )

    return render(request, 'produit/produits_all.html', {'age': age })


def prix(request):
        valeur = request.GET.get("b",'0,2000')
        search = request.GET.get('q')
        categorie = request.GET.get('categorie')
        time = request.GET.get('time')
        valeur = valeur.split(',')
        min1 =int(valeur[0])
        min2 =int(valeur[1])

        user = request.user
        age = user.profile.age
        print(age)
        produit_results = Produit.objects.all()


        if search :
            produit_results  = produit_results.filter(Q(title__icontains=search )| Q(tags__icontains=search))

        if valeur :
            produit_results =  produit_results.filter(prix__gt = min1, prix__lt = min2)
        if categorie :
            produit_results =  produit_results.filter(categorie__contains=categorie)
        if time == 'anciens':
            produit_results = produit_results.order_by('date')
        if  time == 'recent' :
            produit_results = produit_results.order_by('-date')
        if  time == 'prix croissant' :
            produit_results = produit_results.order_by('prix')

        if  time == 'prix decroissant' :
            produit_results = produit_results.order_by('-prix')


        return render(request, 'produit/produits_all.html' , {'produits': produit_results,'bijoux':produit_results.filter(categorie='bijoux').count() ,'bijoux1':produit_results.filter(categorie='maison et ameublement').count(),'bijoux2':produit_results.filter(categorie='vetements').count(),'bijoux3':produit_results.filter(categorie='art et collections').count(),'bijoux4':produit_results.filter(categorie='accessoires').count(),'bijoux5':produit_results.filter(categorie='sacs et bagages').count(),'bijoux6':produit_results.filter(categorie='mariage').count() })


@login_required
def Activer(request,produit_id):
    try:
        produits = Produit.objects.get(pk=produit_id)
        if produits.user == request.user:
           if produits.etat == True :
               produits.etat = False
               produits.save()

               return JsonResponse({'activation ': 'Reussi'})

           else:
             produits.etat = True
             produits.save()
             return JsonResponse({'Desactivation ':'Reussi'})


        else:

         return JsonResponse({'erreur':'Vous n''avez pas le droit de modifier ce produit. '})

    except Produit.DoesNotExist:
     return JsonResponse({'error' : 'object dose not exist'})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'authentication/register.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            welcome_post = '{0} has joined the network.'.format(user.username,
                                                                user.username)
            return redirect('/')

    else:
        return render(request, 'authentication/register.html',
                      {'form': SignUpForm()})


def msg_parametre(request,pk) :
    boutique = Boutique.objects.get(pk=pk)
    if not boutique.users_list.filter(pk = request.user.id).exists()  and request.user.is_authenticated():
        if boutique.user != request.user :
            boutique.users_list.add(request.user)
            Message.send_param_message(from_user=boutique.user , to_user=request.user , message=boutique.message_param)


def create_wishlist(request):
    user = request.user
    wishlists = wish.objects.filter(user=user)
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:
        form = WishListForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user

            wishlist.save()
            return render(request, 'produit/discover_wishlists.html', {'wishlist': wishlist, 'wishlists': wishlists})

        context = {
            "form": form,

        }

        return render(request, 'produit/create_wishlist.html', context, {'wishlists': wishlists})


def detail_collection_view(request, pk):
    if request.method == 'GET':
        collection = request.user.wishlist.get(pk=pk)
        rows = range(0, collection.produit_set.count(), 4)
        return render(request, 'wishlist/detail_collection.html', {'collection': collection, 'rows': rows})



@login_required
def wishlist_view(request):
    wishlists = wish.objects.all()
    return render(request, 'produit/discover_wishlists.html', {'wishlists': wishlists})

@ajax_required
def produits(request):

    produits = Produit.objects.all()
    dump = []
    template = '{0} ({1})'
    for produit in produits:

        dump.append(produit.title)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


def wishlist(request,pk) :
    produit = Produit.objects.get(pk=pk)
    produit.wish.wishlist.add(produit)
