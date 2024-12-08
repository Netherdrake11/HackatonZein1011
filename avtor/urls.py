from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name = 'register'),
    #path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('logout/', views.logout_view, name='logout'),
]