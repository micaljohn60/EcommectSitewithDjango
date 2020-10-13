from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from.models import Item,Order,OrderItem,Address,Payment,Notification
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from .forms import PaymentForm,AddressForm
import random
# Create your views here.

class HomeView(ListView):    
    def get(self,*args,**kwargs):
        
        order = Order.objects.filter(ordered=True,pending=True).count()
        ordered_count = Order.objects.filter(ordered=True,pending=False).count()
        items = Item.objects.all()
        items_count = Item.objects.all().count()
        
        context = {
            'object_list' : items,
            'order_count' : order,
            'items_count' : items_count,
            'ordered_count' : ordered_count
        }
        return render(self.request,'product_lists.html',context)
    

class ProductDetailView(View):
    def get(self,request,slug):
        
        item = Item.objects.get(slug=slug)
        items = Item.objects.all()[:3]         
        context = {
            'object' : item,
            'items'  : items
        }
        return render(request,'product_detail.html',context)
    
class Order_Summary(View):
    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order-summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

def add_to_cart(request, slug):   
    item = Item.objects.get(slug=slug)    
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():        
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1      
            item.product_quantity -= 1
            item.save()              
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:  
            item.product_quantity -= 1
            item.save()          
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:        
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")\

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            item.product_quantity += order_item.quantity
            item.save()
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)



def remove_single_item_from_cart(request, slug):
    item = Item.objects.get(slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                item.product_quantity += 1
                item.save()
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:productlists", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:productlists", slug=slug)

class CheckOutView(View):
    def get(self,*args,**kwargs):
        address_form = AddressForm()
        payment_form = PaymentForm()
        try:
            address = Address.objects.filter(user=self.request.user)
            order = Order.objects.get(user=self.request.user,ordered=False)
            if address.exists():
                context = {
                    'payment_form' : payment_form,
                    'address':address
                }
                return render(self.request,'check-out.html',context)
            else:         
                context = {
                    'address_form':address_form,
                    'address':address
                }      
                return render(self.request,'check-out.html',context)
            return render(self.request,"check-out.html",context)
        except ObjectDoesNotExist:
            return redirect('core:check-out')
    
    def post(self,*args,**kwargs):        
        add_form = AddressForm(self.request.POST or None)
        payment_form = PaymentForm(self.request.POST,self.request.FILES or None)
        try:
            address = Address.objects.filter(user=self.request.user)
            order = Order.objects.filter(user=self.request.user,ordered=False)    
            order_item = OrderItem.objects.filter(user=self.request.user,ordered=False) 
            if address.exists():
                if payment_form.is_valid():
                    payment_opt = payment_form.cleaned_data.get(
                        'payment_opition'
                    )
                    payment_file =  payment_form.cleaned_data.get(
                        'file'
                    )
                    payment = Payment(
                        user= self.request.user,
                        payment_opition= payment_opt,
                        payment_img = payment_file,                        
                    )                              
                    
                    payment.save()
                    order.update(ordered=True,payment=payment.pk)                    
                    order_item.update(ordered=True)
                    return redirect("core:order-snippet")                 
                    
            else:                
                if add_form.is_valid():
                    address1 = add_form.cleaned_data.get(
                        'address'
                    )
                    address2 = add_form.cleaned_data.get(
                        'address_2'
                    )
                    cities_states = add_form.cleaned_data.get(
                        'cities_state'
                    )
                    bill_address = Address(
                        user = self.request.user,
                        street_address =  address1,
                        apartment_address = address2,
                        cities_state = cities_states                        
                    )
                    bill_address.save()
                    return redirect('core:check-out')                
        
        except ObjectDoesNotExist:  
             return redirect('core:order-summary')

def order_snippet_view(request):
    order = Order.objects.filter(user=request.user,ordered=True,pending=True)
    order1 = Order.objects.filter(user=request.user,ordered=True,pending=False)
    context = {
        'objects':order,
        'objects1':order1
    }
    return render(request,'order-snippet.html',context)

def veiw_ordered_items_lists(request,slug):
    order = Order.objects.filter(ref_code=slug)
    context = {
        'order' : order
    }
    return render(request,'view-ordered.html',context)

def notifications(request):
    notis = Notification.objects.all().order_by('-date')
    context = {
        'notis' : notis
    }
    notis.update(opened=True)
    return render(request,'notifications.html',context)