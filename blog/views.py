from django.shortcuts import render
from django.http import HttpResponse

def post_detail(request, slug):
    return HttpResponse(f"Aqui estão os detalhes do post com slug {slug}.")
