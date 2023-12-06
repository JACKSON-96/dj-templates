from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Outros padrões de URL para o aplicativo do blog
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()