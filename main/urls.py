from django.urls import path
from main import views

urlpatterns = [
    # This is admin page link url
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('system_admin/', views.admin, name='admin'),
    path('search/', views.search, name='search'),
    path('home/<int:pk>', views.home, name='home'),
    path('balance/<int:pk>', views.AddBalance, name='balance_url'),
    path('update_balance/',views.UpdateBalance, name='update_balance_url'),
    path('permition/<int:id>', views.permition, name='permition'),
    path('payment/', views.payment, name='payment'),
    path('postData/<str:meterNO>',views.postData,name='postData'),
]