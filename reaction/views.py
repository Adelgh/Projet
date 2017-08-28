# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from notification.models import Notification
from post.models import Post, Commentaire
from produit.models import Produit
from website.decorators import ajax_required
from reaction.models import Reaction, Post_Reaction, Commentaire_Reaction


@login_required
@ajax_required
def react(request, pk):
    data = {}
    product = Produit.objects.get(pk=pk)
    reaction = request.GET.get('reaction')
    has_reacted = Reaction.objects.filter(user=request.user, product=product).count() == 1
    reaction_choices = Reaction.get_choices()

    if has_reacted:
        reaction_obj = request.user.reaction_set.get(product=product)

        if reaction in reaction_choices:
            if reaction_obj.type != reaction:

                reaction_obj.type = reaction
                reaction_obj.save()

                Notification.send(from_user=request.user, to_user=product.boutique.user, product=product,
                                  type=reaction)
            else:
                reaction_obj.delete()

            data['product'] = reaction

        elif not reaction:
            reaction_obj.delete()
            data['product'] = ''

    elif reaction in reaction_choices:
        Reaction.objects.create(user=request.user, product=product, type=reaction)
        if request.user != product.boutique.user :
            Notification.send(from_user=request.user, to_user=product.boutique.user, product=product, type=reaction)

        data['product'] = reaction



    data['count'] = product.reaction_set.count()
    return HttpResponse(json.dumps(data), content_type='application/json' )



@login_required
@ajax_required
def post_react(request, pk):
    data = {}
    post = Post.objects.get(pk=pk)
    reaction = request.GET.get('reaction')
    has_reacted = Post_Reaction.objects.filter(user=request.user, post=post).count() == 1
    reaction_choices = Post_Reaction.get_choice()

    if has_reacted:
        reaction_obj = request.user.post_reaction_set.get(post=post)

        if reaction in reaction_choices:
            if reaction_obj.type != reaction:
                reaction_obj.type = reaction
                reaction_obj.save()
                Notification.send_post(from_user=request.user, to_user=post.user, post=post, type=reaction)
            else:
                reaction_obj.delete()
            data['reaction'] = reaction
        elif not reaction:
            reaction_obj.delete()
            data['reaction'] = ''
    elif reaction in reaction_choices:
        Post_Reaction.objects.create(user=request.user, post=post, type=reaction)
        if request.user != post.user :

            Notification.send_post(from_user=request.user, to_user=post.user, post=post, type=reaction)
        data['reaction'] = reaction



    data['like_count'] = post.get_likes_count()
    data['dislike_count'] = post.get_dislikes_count()

    return HttpResponse(json.dumps(data), content_type='application/json' )




