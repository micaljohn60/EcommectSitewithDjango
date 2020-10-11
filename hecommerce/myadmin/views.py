from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.models import Item,Order,OrderItem,Payment,Notification
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.models import User
from django.contrib import messages
from .import forms

# Create your views here.
class UploadProduct(View):
    def get(self,*args,**kwargs):
        form = forms.UploadProductForm()
        context = {
            'form':form
        }
        return render(self.request,'upload-product.html',context)
    
    def post(self,*args,**kwargs):
        form = forms.UploadProductForm(self.request.POST,self.request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data.get(
                'title'
            )
            price = form.cleaned_data.get(
                'price'
            )
            slug = form.cleaned_data.get(
                'slug'
            )
            product_quantity = form.cleaned_data.get(
                'product_quantity'
            )
            description = form.cleaned_data.get(
                'description'
            )
            category = form.cleaned_data.get(
                'category'
            )
            label = form.cleaned_data.get(
                'label'
            )
            image = form.cleaned_data.get(
                'image'
            )
            save_item = Item(
                title=title,
                price=price,
                category=category,
                label=label,
                product_quantity=product_quantity,
                description=description,
                slug=slug,
                image=image                
            )
            save_item.save()
            messages.info(self.request,"Item Has Been Added")
            return redirect("myadmin:upload-product")
        form = forms.UploadProductForm()
        context = {
            'form':form
        }
        return render(self.request,'upload-product.html',context)   
    
class PendingOrders(View):
    def get(self,*args,**kwargs):      
        
        payments = Payment.objects.all()            
        orders = Order.objects.filter(pending=True,ordered=True)        
        order_items = OrderItem.objects.filter(ordered=True)                     
        context = {
            'orders' : orders,
            'order_items':order_items,
            'payment':payments
        }
        return render(self.request,'pending-orders.html',context)
    
def pending_order_detail_view(request,slug):
    payments = Payment.objects.all() 
    orders = Order.objects.filter(ref_code=slug,ordered=True,pending=True)
    context = {
        'orders': orders,
        'payments':payments
    }
    return render(request,'pending-order-detail.html',context)

def pending_order_confirm(request,slug):
    order = Order.objects.filter(ref_code=slug,ordered=True,pending=True)
    for orde in order:
        noti = Notification(user=orde.user,notification_title="Your order "+ slug +"has been confirmed")
        noti.save()
    order.update(pending=False)
    messages.info(request,slug + "has Confirmed")
    return redirect('myadmin:pendingorders')

def pending_order_reject(request,slug):
    order = Order.objects.filter(ref_code=slug,ordered=True,pending=True)
    for orde in order:
        noti = Notification(user=orde.user,notification_title="Your order "+ slug +"has been rejected dut to incomplete information")
        noti.save()
    order.delete()
    messages.warning(request,slug + "has Rejected")
    return redirect('myadmin:pendingorders')

def view_ordered(request):
    orders = Order.objects.filter(ordered=True,pending=False).order_by('ordered_date')
    context = {
        'orders':orders
    }
    return render(request,'ordered.html',context)
    
class UpdateProductList(ListView):
    model = Item
    template_name = 'update-product-list.html'

class UpdateProduct(View):
    def get(self,request,slug):
        
        item = Item.objects.get(slug=slug)
        form = forms.UpdateForm(instance=item)
        context = {
            'form' : form ,
            'item' : item
        }
        return render(self.request,'update-product.html',context)
    
    def post(self,request,slug):        
        item = Item.objects.get(slug=slug)
        form = forms.UpdateForm(self.request.POST,self.request.FILES,instance=item)   
        if form.is_valid():
            form.save()
            messages.info(request,item.title + "is updated")
            return redirect("myadmin:updateproductlist")
        
        return render(self.request,'update-product-list.html')
#need to fix
def delete_product(request,slug):
    item = Item.objects.get(slug=slug)
    messages.info(request,item.title + "is delected")
    item.delete()    
    return redirect("myadmin:updateproductlist")


        
        
        
        
        
            
            
    