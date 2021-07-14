from django.urls import path
from .import views
urlpatterns = [
    path('',views.sign_in,name="sign_in"),
    path('register/',views.register,name="register"),
    path('sign_out/',views.sign_out,name="sign_out"),
    path('index/',views.index,name="index")
]