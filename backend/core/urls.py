from .views import *
from django.urls import path

urlpatterns = [
    path('<slug:slug>/', PortfolioView.as_view(), name='portfolio'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout')

]