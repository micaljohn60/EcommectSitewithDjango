from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from account.views import login_view,signup_view,VerificationView,logout_view

# Create your tests here.

class UrlTest(SimpleTestCase):
    
    def test_signup(self):
        url = reverse('account:sign_up')
        self.assertEquals(resolve(url).func,signup_view) 
    
    def test_login(self):
        url = reverse('account:log_in')
        self.assertEquals(resolve(url).func,login_view)   
        
    def test_Verification(self):
        url = reverse('account:activate', args=['(?P<uidb64>[^/]+)','/(?P<token>[^/]+)$'])
        self.assertEquals(resolve(url).func.view_class,VerificationView)
        
    def test_logout(self):
        url = reverse('account:log_out')
        self.assertEquals(resolve(url).func,logout_view)
