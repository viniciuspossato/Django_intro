from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):

    # Aqui, estamos preparando uma função que nos permite
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'publicado')

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),
    )

    # O que existe em nossa postagem? Título, Autor, Slug e o Corpo/Conteúdo...

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    conteudo = models.TextField() # Campo com muito conteúdo

    publicado = models.DateField(default = timezone.now) # Data de publicação: Agora!
    criado = models.DateField(auto_now_add = True) # Apenas na criação ele será setado
    alterado = models.DateField(auto_now=True) # Sempre que for atualizado, a hora muda

    status = models.CharField(choices=STATUS,
                              max_length=10,
                              default='rascunho')

    class Meta:
        ordering = ('-publicado',) # ordenando as postagens de acordo com a data de pubkicação

    def __str__(self): # Dando às postagens os seus títulos
        return '{} - {}'.format(self.titulo,self.autor)

    # Inserindo o novo manager (Published)
    objects = models.Manager()  # Permitindo com que o objects possa ser utilizado também
    published = PublishedManager()

# Create your models here.

