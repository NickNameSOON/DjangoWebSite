from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('forms', views.forms),
    path('about-us', views.about),
    path('submit', views.submit)
]