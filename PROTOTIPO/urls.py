from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('sistema/', views.sistema, name="sistema"),
    path('camara', views.camara, name="camara"),
]