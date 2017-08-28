import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from website.decorators import is_wishcollection_owner, ajax_required
from wishlist.models import WishCollection
from wishlist.forms import WishCollectionForm
from produit.models import Produit


@login_required
def wishlist_view(request):
    collections = request.user.wishlist.collections.all()
    return render(request, 'wishlist/wishlist.html', {'collections': collections, 'wishlistuser': request.user})



@login_required
def user_wishlist_view(request, pk):
    user = User.objects.get(pk=pk)
    collections = WishCollection.objects.filter(wishlist__user__id=pk)
    return render(request, 'wishlist/wishlist.html', {'collections': collections, 'wishlistuser': user})



@login_required
def detail_collection_view(request, pk):
    if request.method == 'GET':
        collection = WishCollection.objects.get(pk=pk)
        rows = range(0, collection.produit_set.count(), 4)
        return render(request, 'wishlist/detail_collection.html', {'collection': collection, 'rows': rows})



@login_required
@ajax_required
def new_collection_view(request):
    if request.method == 'POST':
        form = WishCollectionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.wishlist = request.user.wishlist
            obj.save()
            context = {
                'success': True,
                'collection': render_to_string('wishlist/includes/collection.html', {'collection': obj, 'new': True})
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
    return HttpResponse()



@login_required
@is_wishcollection_owner
@ajax_required
def delete_collection_view(request, pk):
    if request.method == 'POST':
        WishCollection.objects.get(pk=pk).delete()
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    return HttpResponse()



@login_required
@is_wishcollection_owner
@ajax_required
def add_product_view(request, pk, produit_id):
    if request.method == 'POST':
        collection = request.user.wishlist.collections.get(pk=pk)
        product = Produit.objects.get(pk=produit_id)
        collection.produit_set.add(product)
        return HttpResponse(json.dumps({'success': True, 'checked': True}), content_type='application/json')
    return HttpResponse()




@login_required
@is_wishcollection_owner
@ajax_required
def remove_product_view(request, pk, produit_id):
    if request.method == 'POST':
        collection = request.user.wishlist.collections.get(pk=pk)
        product = Produit.objects.get(pk=produit_id)
        if product in collection.produit_set.all():
            collection.produit_set.remove(product)
        return HttpResponse(json.dumps({'success': True, 'checked': False, 'count': collection.produit_set.count()}), content_type='application/json')
    return HttpResponse()