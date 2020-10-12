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
    make_unavaliable_product,
    make_product_avaliable
)

app_name = "myadmin"
urlpatterns = [
    path('admins/',UploadProduct.as_view(),name="upload-product"),
    path('pending-orders/',PendingOrders.as_view(),name="pendingorders"),    
    path('view-ordered/',view_ordered,name="viewordered"),
    path('update-product/',UpdateProductList.as_view(),name="updateproductlist"),
    path('unavaliable-product/<slug>',make_unavaliable_product,name="unavaliableproduct"),
    path('make-avaliable-product/<slug>',make_product_avaliable,name="makeproductavaliable"),
    path('update-product/<slug>',UpdateProduct.as_view(),name="updateproduct"),
    path('pending-orders-detail/<slug>/',pending_order_detail_view,name="pendingdetail"),
    path('pending-orders-confirm/<slug>/',pending_order_confirm,name="pendingorderconfirm"),
    path('pending-orders-reject/<slug>',pending_order_reject,name="pendingorderreject")
    
]