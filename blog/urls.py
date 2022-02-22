from django.urls import path
from . import views

# Tomando um padrão de URL
urlpatterns = [
    path('', views.BlogListView.as_view(), name='home')
]