"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Ajustes para utilizar enquanto desenvolvimento apenas, pois quando em produção, DEBUG = false
from django.conf import settings  # Iremos importar informações do script settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    #Fazemos isso para abrirmos as imagens enquanto o projeto não está em produção
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

