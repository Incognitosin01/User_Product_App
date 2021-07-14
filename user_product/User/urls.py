from django.urls import path
from .import views
urlpatterns = [
    path('',views.sign_in,name="sign_in"),
    path('register/',views.register,name="register"),
    path('sign_out/',views.sign_out,name="sign_out"),
    path('createPost/',views.post_create,name="post_create"),
    path('index/',views.index,name="index"),
    path('postData/',views.post_data,name="view_posts"),
    path('deletePost/<int:pk>',views.post_delete,name='post_delete'),
    path('updatePost/<int:pk>',views.post_update,name="post_update")
]