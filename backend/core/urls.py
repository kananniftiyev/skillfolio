from .views import *
from django.urls import path
from core.docs import schema_view


urlpatterns = [
    path('portfolio/<slug:slug>/', PortfolioView.as_view(), name='portfolio'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user', UserDetailView.as_view(), name='user'),
    path('portfolio', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('project', ProjectView.as_view(), name='project-create'),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]