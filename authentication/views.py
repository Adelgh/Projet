import json

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from authentication.forms import ProfileForm
from produit.forms import SignUpForm
from produit.models import Produit, Boutique
from authentication.models import Profile
from produit.models import Boutique

def logout_user(request):
    logout(request)
    form = SignUpForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'authentication/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        users_produits = Produit.objects.all()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/boutique/produits')
            else:
                return render(request, 'authentication/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Invalid login'})
    return render(request, 'authentication/login.html')


def register(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                boutiques = Boutique.objects.filter(user=request.user)
                return render(request, 'produit/index.html', {'boutique': boutiques})
    context = {
        "form": form,
    }
    return render(request, 'authentication/register.html', context)


@login_required
def edit_user_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            obj = form.save(commit=False)
            request.user.username = request.POST['username'] or request.user.username
            request.user.save()
            obj.save()
        return render(request, 'authentication/profile.html')

    form = ProfileForm(instance=request.user.profile)
    if  request.user.username :
        return render(request, 'authentication/edit_profile.html', {'form': form })
    else:
        return render(request, 'authentication/notuser.html')

@login_required
def profile(request, username):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            obj = form.save(commit=False)
            request.user.username = request.POST['username'] or request.user.username
            request.user.save()
            obj.save()
        return render(request, 'authentication/profile.html')

    form = ProfileForm(instance=request.user.profile)
    page_user = User.objects.get(username=username)
    data = {
        'page_user': page_user,
        'page': 1 ,
        'form': form
    }

    return render(request, 'authentication/profile.html', data )

@login_required
def friend_invite(request):
        if request.method == 'POST':
            form = FriendInviteForm(request.POST)
            if form.is_valid():
             invitation = Invitation(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                code=User.objects.make_random_password(20),
                sender=request.user
                )
             invitation.save()
             invitation.send()
            return HttpResponseRedirect('/friend/invite/')
        else:
            form = FriendInviteForm()
            variables = RequestContext(request, {
            'form': form
            })
        return render_to_response('friend_invite.html', variables)