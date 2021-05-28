from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [


    path('detail/', views.u1net_detail_view),
    # path('', home )


]