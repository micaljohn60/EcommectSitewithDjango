from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('E', 'Electronic'),
    ('S', 'Shirt'),
    ('U', 'Utility')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
    ('N', 'None')
)

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    product_quantity = models.IntegerField(null=False,blank=False,default=0)
    slug = models.SlugField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })       
    
    
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item(self):
        return self.quantity
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):
        return self.get_total_item_price()

class Order(models.Model):
    def get_ref_code():
        last_ref_code = Order.objects.all().order_by('id').last()
        if not last_ref_code:
            return 'INV-000-1'
        invoice_no = last_ref_code.ref_code
        invoice_int = int(invoice_no.split('-')[2])
        new_invoice_int = invoice_int + 1
        new_invoice_no = 'INV-000-' + str(new_invoice_int)
        return new_invoice_no


    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True,default=get_ref_code)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    payment = models.ForeignKey('Payment',on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.user.username  
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
    def get_item_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item()
        return total
        
    
    
CITIES_STATE = (
    ('kachin','Kachin'),
    ('kaya','Kaya'),
    ('Kayin','Kayin'),
    ('chin','Chin'),
    ('mon','Mon'),
    ('yangon','Yangon'),
    ('naypyitaw','Nay Pyi Taw'),
    ('Mandalay','Mandalay'),
    ('rakhine','Rakhine')
    
)

PAYMENT_CHOICES = (
    ('cbpay','CB Pay'),
    ('kbzpay','KBZ Pay'),
    ('ayapay','AYA Pay'),
    ('cbbank','CB Bank Transfer'),
    ('kbzbank','KBZ Bank Transfer'),
    ('ayabank','AYA Bank Transfer')
)

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    cities_state = models.CharField(choices=CITIES_STATE, max_length=11)
    
    def __str__(self):
        return self.user.username  
    
class Payment(models.Model):
    def get_ref_code():
        last_ref_code = Payment.objects.all().order_by('id').last()
        if not last_ref_code:
            return 'INV-000-1'
        invoice_no = last_ref_code.payment_ref_code
        invoice_int = int(invoice_no.split('-')[2])
        new_invoice_int = invoice_int + 1
        new_invoice_no = 'INV-000-' + str(new_invoice_int)
        return new_invoice_no
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    payment_opition =  models.CharField(choices=PAYMENT_CHOICES,max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_img = models.ImageField()
    payment_ref_code = models.CharField(max_length=20, blank=True, null=True,default=get_ref_code)
    
    
    def __str__(self):
        return self.user.username
    
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notification_title = models.CharField(max_length=100,blank=True,null=True)    
    opened = models.BooleanField(default=False)
    success_fail = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
    
