from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation),
    path('usage/', views.usage),
    path('topup/', views.meterTopup),
]