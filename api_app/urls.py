from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentation),
    path('post/', views.post),
]