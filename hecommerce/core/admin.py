from django.contrib import admin
from.models import Item,Order,OrderItem,Address,Payment,Notification,NewsLetter
# Register your models here.
admin.site.register(Item)
admin.site.register(Order),
admin.site.register(OrderItem),
admin.site.register(Address),
admin.site.register(Payment),
admin.site.register(Notification)
admin.site.register(NewsLetter)
