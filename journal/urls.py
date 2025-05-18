from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_paper, name='submit_paper'),
    path('archive/', views.archive, name='archive'),
    path('authors/', views.authors, name='authors'),
    path('author-login/', views.author_login, name='author_login'),
    path('author-logout/', views.author_logout, name='author_logout'),
    path('author-register/', views.author_register, name='author_register'),
    path('call-for-paper/', views.call_for_paper, name='call_for_paper'),
    path('track/', views.track_paper, name='track_paper'),
] 