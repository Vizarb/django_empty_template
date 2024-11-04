from django.urls import path
from . import views
from .views import RegisterView, LoginView, LogoutView 

urlpatterns = [
    path('', views.index, name='index'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
