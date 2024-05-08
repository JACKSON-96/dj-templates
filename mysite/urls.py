from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='admin:login')),
    path('blog/', include('blog.urls')),  # Rotas do aplicativo de blog
    path('home/', include('blog.urls')),  # Adiciona a rota para /home e redireciona para o arquivo de URLs do seu aplicativo
]
