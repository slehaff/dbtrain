from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
   
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('detail/', views.u1net_detail_view),

]