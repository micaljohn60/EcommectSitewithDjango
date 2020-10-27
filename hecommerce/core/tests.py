from django.test import SimpleTestCase,TestCase,Client,RequestFactory
from core.views import HomeView,ProductDetailView,Order_Summary,add_to_cart,remove_from_cart,Order_Summary
from django.urls import reverse,resolve
from core.models import Item
from django.contrib.auth.models import AnonymousUser

# Create your tests here.
# Test Urls 
class TestUrls(SimpleTestCase):
    def test_core_HomeView_url(self):
        url = reverse('core:productlists')
        self.assertEquals(resolve(url).func.view_class,HomeView)
    
    def test_core_productDetailView_url(self):
        url = reverse('core:productdetail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class,ProductDetailView)
        
    def test_core_Order_Summary_url(self):
        url = reverse('core:order-summary')
        self.assertEquals(resolve(url).func.view_class,Order_Summary)  
        
    def test_core_add_to_cart_url(self):
        url = reverse('core:add-to-cart', args=['some-args'])
        self.assertEquals(resolve(url).func,add_to_cart)
          
    def test_core_remove_from_cart(self):
        url = reverse('core:remove-from-cart', args=['some-args'])
        self.assertEquals(resolve(url).func,remove_from_cart)

    def test_core_order_summary(self):
        url = reverse('core:order-summary')
        self.assertEquals(resolve(url).func.view_class,Order_Summary)
        
    
        
        