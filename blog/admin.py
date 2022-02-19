from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # Lista de exibição
    list_display = ('titulo','autor','conteudo','publicado','status')

    # Aba de pesquisa de posts
    search_fields=('titulo','conteudo')

    # Preenchimento automático do slug de acordo com o titulo
    prepopulated_fields = {'slug' : ('titulo',)}

    # Inserindo aba lateral de filtros
    list_filter = ('status','criado','publicado','autor')

    # Incluindo aba de pesquisa detalhada de data
    date_hierarchy = 'publicado'

    # IDs dos autores (funciona na hora de criar posts)
    raw_id_fields = ('autor',)

# Register your models here.
