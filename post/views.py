from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import Post, Commentaire, Categorie
from notification.models import Notification
from post.forms import PostForm, CategorieForm, CommentaireForm
from produit.models import Produit


def post(request):
    user = request.user
    if request.method == 'POST':
        form1 = PostForm(request.POST, request.FILES)
        if form1.is_valid() :
            post = form1.save(commit=False)
            post.user = request.user
            post.save()
            return render(request, 'post/post.html' ,{'post' : post})

    form1 = PostForm()
    posts = Post.objects.filter(user = user)
    return render(request, 'post/postForm.html', {'form': form1 ,'posts' : posts})


def all_posts(request):
    posts = Post.objects.all()
    form = CommentaireForm()
    return render(request, 'post/all_posts.html', {'posts' : posts, 'form': form ,'bijoux': posts.filter(categorie__name='bijoux').count(),
                   'bijoux1': posts.filter(categorie__name='maison et ameublement').count(),
                   'bijoux2': posts.filter(categorie__name='vetements').count(),
                   'bijoux3': posts.filter(categorie__name='art et collections').count(),
                   'bijoux4': posts.filter(categorie__name='accessoires').count(),
                   'bijoux5': posts.filter(categorie__name='sacs et bagages').count(),
                   'bijoux6': posts.filter(categorie__name='mariage').count()})

def user_posts(request,post_id):
    posts = Post.objects.filter(id = post_id)
    form = CommentaireForm()

    return render(request, 'post/all_posts.html', {'posts' : posts , 'form': form  })

def user_post(request,username):
    posts = Post.objects.filter(user__username = username)
    form = PostForm()

    return render(request, 'post/filter.html', {'posts' : posts , 'form': form ,'bijoux': posts.filter(categorie__name='bijoux').count(),
                   'bijoux1': posts.filter(categorie__name='maison et ameublement').count(),
                   'bijoux2': posts.filter(categorie__name='vetements').count(),
                   'bijoux3': posts.filter(categorie__name='art et collections').count(),
                   'bijoux4': posts.filter(categorie__name='accessoires').count(),
                   'bijoux5': posts.filter(categorie__name='sacs et bagages').count(),
                   'bijoux6': posts.filter(categorie__name='mariage').count() })
def comment(request, post_id):
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        reaction = request.GET.get('comment')

        post = Post.objects.get(pk=post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            if request.user != comment.user:
                Notification.send_comment(from_user=request.user, to_user=comment.user, comment=comment, type=reaction)

            return render(request, 'post/comment.html', {'comment': comment})

    form = CommentaireForm()
    comments = Commentaire.objects.all()
    return render(request, 'post/commentaire.html', {'form': form, 'comments': comments})


def categorie(request):
    user = request.user
    if request.method == 'POST':
        form = CategorieForm(request.POST, request.FILES)
        if form.is_valid() :
            obj = form.save(commit=False)
            obj.save()
            return render(request, 'post/post.html' ,{'categorie' : obj})

    form = CategorieForm()

    posts = Post.objects.filter(user = user)
    return render(request, 'post/postForm.html', {'form': form ,'posts' : posts})



def Acceuil(request):
    list_produit = Produit.objects.filter()[:4]
    posts = Post.objects.filter()[:4]

    return render(request, 'post/Acceuil.html',{'produits':list_produit,'posts' : posts})

def categoriefilter(request):
    post_results = Post.objects.all()
    categorie = request.GET.get('categorie__name')
    print (categorie)
    form = PostForm()
    if categorie  :
        post_results = post_results.filter(categorie__name__contains=categorie)


    return render(request, 'post/filter.html',
                  {'posts': post_results,'form': form,'bijoux': post_results.filter(categorie__name='bijoux').count(),
                   'bijoux1': post_results.filter(categorie__name='maison et ameublement').count(),
                   'bijoux2': post_results.filter(categorie__name='vetements').count(),
                   'bijoux3': post_results.filter(categorie__name='art et collections').count(),
                   'bijoux4': post_results.filter(categorie__name='accessoires').count(),
                   'bijoux5': post_results.filter(categorie__name='sacs et bagages').count(),
                   'bijoux6': post_results.filter(categorie__name='mariage').count()})
