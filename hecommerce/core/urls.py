from django.urls import path,re_path
from.views import(
    HomeView,
    ProductDetailView,
    add_to_cart,
    Order_Summary,
    remove_single_item_from_cart,
    remove_from_cart,
    CheckOutView,
    order_snippet_view,
    veiw_ordered_items_lists,
    notifications,
    displayCategory
)

app_name="core"

urlpatterns = [
    path('', HomeView.as_view(),name="productlists"),
    path('order-summary/',Order_Summary.as_view(),name="order-summary"),
    path('check-out/',CheckOutView.as_view(),name="check-out"),
    path('order-snippet/',order_snippet_view,name="order-snippet"),
    path('notifications/',notifications,name="notifications"),
    path('add-to-cart/<slug>/',add_to_cart,name="add-to-cart"), 
    path('remve-from-cart/<slug>/',remove_from_cart,name="remove-from-cart"),
    path('remove-single-item-from-cart/<slug>/',remove_single_item_from_cart,name="remove-single-item-from-cart"),    
    path('view-ordered-items/<slug>/',veiw_ordered_items_lists,name="vieworderedlists"),
    path('category/<category>',displayCategory,name="display-category"),
    re_path(r'(?P<slug>[\w-]+)/$',ProductDetailView.as_view(),name="productdetail"),
    
]
