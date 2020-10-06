from django.urls import path
from.views import (
    signup_view,
    login_view,
    logout_view
)

app_name = "account"

urlpatterns = [
    path('login/',login_view,name="log_in"),
    path('signup/',signup_view,name="sign_up"),
    path('logout/',logout_view,name="log_out")
]