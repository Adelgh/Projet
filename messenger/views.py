import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import redirect, render
from ajax_select import register, LookupChannel

from produit.models import Produit, Commercant, Boutique
from website.decorators import ajax_required
from messenger.models import Message

def get_products(user_id):
    return Produit.objects.filter(produit__commercant__user__pk=user_id)[:3] or Produit.objects.all()[:3]

@login_required
def inbox(request):
    user = request.user
    conversations = Message.get_conversations(user=request.user)
    active_conversation = None

    boutique = Boutique.objects.all()
    boutique1 = boutique.filter(user = user)
    produit1 = Produit.objects.filter(boutique_id=boutique)[:2]

    messages = None
    for person in Commercant.objects.all() :
        person1 = person.user
        if  user.username == str(person1) :

            produit = Produit.objects.filter(boutique_id = boutique1)

        else :
            produit = Produit.objects.filter()
    if conversations:
        conversation = conversations[0]
        active_conversation = conversation['user'].username
        messages = Message.objects.filter(user=request.user,
                                              conversation=conversation['user'])

        messages.update(is_read=True)
        for conversation in conversations:
            if conversation['user'].username == active_conversation:
                    conversation['unread'] = 0

    return render(request, 'messenger/inbox.html', {
            'messages': messages,
            'conversations': conversations,
            'active': active_conversation,
            'produit':produit ,
            'produit1': produit1,

    })


def messages(request, username):
    if not request.user.is_authenticated():
        return render(request, 'authentication/login.html')
    else:

        conversations = Message.get_conversations(user=request.user)
        active_conversation = username
        user = request.user
        messages = Message.objects.filter(user=request.user,conversation__username=username)
        messages.update(is_read=True)
        boutique = Boutique.objects.all()
        boutique1 = boutique.filter(user=user)
        produit1 = Produit.objects.filter(boutique_id=boutique)[:2]

        for person in Commercant.objects.all():
            person1 = person.user
            if user.username == str(person1):

                produit = Produit.objects.filter(boutique_id=boutique1)

            else:
                produit = Produit.objects.filter()

        for conversation in conversations:
            if conversation['user'].username == username:
                conversation['unread'] = 0
                if not  username == Commercant.user :
                        return render(request, 'messenger/inbox.html', {
                            'messages': messages,
                            'conversations': conversations,
                            'active': active_conversation,
                            'produit': produit,
                            'produit1': produit1

                        })
                else :
                    produit = Produit.objects.all()
                    return render(request, 'messenger/inbox.html', {
                        'messages': messages,
                        'conversations': conversations,
                        'active': active_conversation,
                        'produit': produit
                    })
    return render(request, 'messenger/inbox.html', {
                            'messages': messages,
                            'conversations': conversations,
                            'active': active_conversation,
                            'produit': produit

    })





@login_required
def new(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        try:

            to_user = User.objects.get(username=to_user_username)

        except Exception:
            try:

                to_user_username = to_user_username[
                    to_user_username.rfind('(')+1:len(to_user_username)-1]
                to_user = User.objects.get(username=to_user_username)
                message = request.POST.get('message')

            except Exception:
                return redirect('/messages/new')
        message = request.POST.get('message')
        objet = request.POST.get('objet')
        url = request.POST.get('url')
        image = request.POST.get('image')
        produit = request.POST.get('produit.id')


        if from_user != to_user:

            Message.send_message(from_user, to_user, message ,image,objet,url,produit)
        produit2 = request.GET.get('b')
        boutique1 = request.GET.get('z')
        boutique = request.GET.get('po')
        return redirect('/messages/{0}/?z={1}&b={2}&po={3}&a={4}'.format(to_user_username,boutique1, produit2,boutique,image))

    else:
        produit2 = request.GET.get('b')
        boutique1 = request.GET.get('z')


        produit = Produit.objects.filter(boutique_id=produit2)
        produit1 = Produit.objects.filter(pk=boutique1)

        conversations = Message.get_conversations(user=request.user)
        return render(request, 'messenger/new.html',
                      {'conversations': conversations, 'produit' :produit,'produit1' :produit1
                       })


@login_required
@ajax_required
def delete(request):
    return HttpResponse()

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            boutique1 = request.GET.get('z')
            m = Message.objects.get(pk=boutique1)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse()
    return HttpResponseForbidden()

@login_required

def send(request):

    if request.method == 'POST':
        #print('aaaaaa')
        from_user = request.user
        to_user_username = request.POST.get('to')
        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message')
        image = request.FILES.get('image')
        #return HttpResponse()
        objet = None
        url = None
        produit1 =  request.POST.get('produit')
        if produit1 == None :
            produit = None
        else :
            produit = Produit.objects.get(pk=produit1)
        if from_user != to_user :
            msg = Message.send_message(from_user, to_user , message,image,objet,url,produit)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg })

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

@login_required
def send1(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message',None)
        image = request.FILES.get('image',None)

        if from_user != to_user:
            msg = Message.send_image_message(from_user, to_user, message,image)
            return render(request, 'messenger/includes/partial_message.html',
                          {'message': msg })
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
@login_required

def filter(request):
    conversations = Message.get_conversations(user=request.user)
    search = request.GET.get('q')
    produit_results = Produit.objects.all()
    if search:
        produit_results = produit_results.filter(Q(title__icontains=search))
    else :
        produit_results = Produit.objects.all()

    if conversations:
            conversation = conversations[0]
            active_conversation = conversation['user'].username
            messages = Message.objects.filter(user=request.user,
                                              conversation=conversation['user'])

    return render(request, 'messenger/includes/produit-search.html' , {'produit': produit_results ,
                                                                       'active':active_conversation,
                                                                       'message' : messages
                                                                       })


@login_required
@ajax_required
def users(request):
    users = User.objects.filter(is_active=True)
    dump = []
    template = '{0} ({1})'
    for user in users:
        if user.profile.get_screen_name() != user.username:
            dump.append(template.format(user.profile.get_screen_name(),
                                        user.username))
        else:
            dump.append(user.username)
    data = json.dumps(dump)
    return HttpResponse(data, content_type='application/json')


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)




@register('tags')
class TagsLookup(LookupChannel):

    model = Produit

    def get_query(self, q, request):
        return self.model.objects.filter(name=q)

    def format_item_display(self, item):
        return u"<span class='produit'>%s</span>"



@login_required
@ajax_required
def latest(request):
    latest = None
    from_user_id = request.GET.get('from_user')
    if from_user_id:
        from_user = User.objects.get(pk=from_user_id)
        latest = Message.objects.filter(user=request.user, from_user=from_user, is_read=False).last()
        if latest:
            if request.GET.get('is_read'):
                data = {'success': True}
                latest.is_read = True
                latest.save()
    return render(request, 'messenger/includes/partial_message.html', {'message': latest})


