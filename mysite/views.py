from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Nome do arquivo HTML para a página de login personalizada
