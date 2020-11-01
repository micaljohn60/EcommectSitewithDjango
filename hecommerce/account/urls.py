from django.urls import path
from.views import (
    signup_view,
    login_view,
    logout_view,
    VerificationView,
    superuser_login_view
    
)

app_name = "account"

urlpatterns = [
    path('login/',login_view,name="log_in"),
    path('admin-login',superuser_login_view,name="superuserlogin"),
    path('signup/',signup_view,name="sign_up"),
    path('logout/',logout_view,name="log_out"),
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name="activate")
    
]