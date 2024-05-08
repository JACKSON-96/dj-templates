from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView  # Import DetailView
from django.shortcuts import render
from blog.models import Post

class HomeView(TemplateView):
    template_name = "home.html"
    
class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

def sobre(request):
    return HttpResponse("Esta é a página Sobre nós.")

def politica(request):
    return render(request, 'blog/politica.html')

def contato(request):
    return render(request, 'blog/contato.html')

def post_detail(request, slug):
    return HttpResponse(f"Aqui estão os detalhes do post com slug {slug}.")
