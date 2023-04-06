from django.urls import path
from . import views

app_name = 'argusdorker'

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('user/', views.user_view, name='user'),
    path('check_domain/', views.check_domain, name='check_domain'),
    path('stats/', views.get_stats, name='get_stats'),
]