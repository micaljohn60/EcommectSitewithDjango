from django.urls import path,re_path
from.views import(
    UploadProduct,
    PendingOrders,
    pending_order_detail_view,
    pending_order_confirm,
    view_ordered,
    pending_order_reject,
    UpdateProductList,
    UpdateProduct,
    view_ordered_detail,
    addnewsletter
)

app_name = "myadmin"
urlpatterns = [
    path('admins/',UploadProduct.as_view(),name="upload-product"),
    path('pending-orders/',PendingOrders.as_view(),name="pendingorders"),    
    path('view-ordered/',view_ordered,name="viewordered"),
    path('add-newsletter',addnewletter,name="addnewsletters"),
    path('ordered_dtail/<slug>',view_ordered_detail,name="ordered-detail"),
    path('update-product/',UpdateProductList.as_view(),name="updateproductlist"),
    path('update-product/<slug>',UpdateProduct.as_view(),name="updateproduct"),
    path('pending-orders-detail/<slug>/',pending_order_detail_view,name="pendingdetail"),
    path('pending-orders-confirm/<slug>/',pending_order_confirm,name="pendingorderconfirm"),
    path('pending-orders-reject/<slug>',pending_order_reject,name="pendingorderreject")
    
]