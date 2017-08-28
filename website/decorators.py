from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse_lazy

from wishlist.models import WishCollection


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap



def is_wishcollection_owner(f):
    def wrap(request, *args, **kwargs):
        collection = WishCollection.objects.get(pk=kwargs['pk'])
        if not collection.wishlist.user == request.user:
            return HttpResponseRedirect(reverse_lazy('welcome'))

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap