from django.contrib import admin
from django.urls import include,path
from index.views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('',index.as_view(),name='index'),
        path('login/',auth_views.LoginView.as_view(template_name="index/Log-in.html"),name="login"),
        path('logout/',auth_views.LogoutView.as_view(template_name="index/Log-in.html"),name="logout"),
]