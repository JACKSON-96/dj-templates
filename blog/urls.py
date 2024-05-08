# urls.py

from django.urls import path
from .views import HomeView, PostDetail, post_detail  # Import post_detail function
from . import views 

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<slug:slug>/", post_detail, name="post_detail"),  # Use post_detail diretamente, pois é uma função de visualização
    path('saiba_mais/', views.sobre, name='saiba_mais'),  # Defina a rota para a view 'sobre' com o nome 'sobre'
    path('sobre/', views.sobre, name='sobre'),
    path('politica/', views.politica, name='politica'),
    path('contato/', views.contato, name='contato'),


]
