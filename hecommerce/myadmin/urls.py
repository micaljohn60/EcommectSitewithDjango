from django.urls import path,re_path
from.views import(
    UploadProduct,
    PendingOrders,
    pending_order_detail_view,
    pending_order_confirm,
    view_ordered,
    pending_order_reject,
    update_product
)

app_name = "myadmin"
urlpatterns = [
    path('admins/',UploadProduct.as_view(),name="upload-product"),
    path('pending-orders/',PendingOrders.as_view(),name="pendingorders"),    
    path('view-ordered/',view_ordered,name="viewordered"),
    path('update-product/',update_product,name="updateproduct"),
    path('pending-orders-detail/<slug>/',pending_order_detail_view,name="pendingdetail"),
    path('pending-orders-confirm/<slug>/',pending_order_confirm,name="pendingorderconfirm"),
    path('pending-orders-reject/<slug>',pending_order_reject,name="pendingorderreject")
    
]