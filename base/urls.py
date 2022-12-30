from django.urls import path
from . import views
urlpatterns = [
    path('auth/', views.userAuth, name='auth'),
    path('', views.home, name='home'),
]