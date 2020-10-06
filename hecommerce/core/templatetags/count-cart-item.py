from django import template
from core.models import Order,Notification

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        order_qs = Order.objects.filter(user=user,ordered=False)
        if order_qs.exists():
            return order_qs[0].items.count()
    return 0

@register.filter
def notification_count(user):
    if user.is_authenticated:
        notis = Notification.objects.filter(user=user,opened=False).order_by('date')
        if notis.exists():
            return notis.count()
    return 0    
