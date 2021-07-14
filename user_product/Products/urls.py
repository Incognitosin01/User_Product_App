from django.urls import path
from .import views
urlpatterns = [
    path('createProduct/',views.product_create,name="product_create"),
    path('productData/',views.product_data,name="view_products"),
    path('deleteProduct/<int:pk>',views.product_delete,name='product_delete'),
    path('updateProduct/<int:pk>',views.product_update,name="product_update")
]