from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_paper, name='submit_paper'),
    path('archive/', views.archive, name='archive'),
] 