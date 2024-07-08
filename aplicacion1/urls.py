from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('quienesSomos',views.quienesSomos, name="quienesSomos"),
    path('servicios',views.servicios, name="servicios"),
]