from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from website.decorators import ajax_required
from .models import Notification


@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)

    unread = Notification.objects.filter(to_user=user, is_read=False)
    for notification in unread:
        notification.is_read = True
        notification.save()

    return render(request, 'notification/notifications.html',
                  {'notifications': reversed(notifications)})




@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:3]
    count = Notification.objects.filter(to_user=user, is_read=False).count()


    return render(request, 'notification/check.html',
                  {'notifications': reversed(notifications), 'count' : count})

@login_required
@ajax_required
def count_notifications(request):
    user = request.user

    count = Notification.objects.filter(to_user=user, is_read=False).count()

    return HttpResponse(count)