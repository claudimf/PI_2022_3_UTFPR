from django.contrib.auth.models import AbstractUser
from django.db import models

from .utils import redimensionar, adicionar_marca_dagua, aplicar_tons_verde


class User(AbstractUser):
    avatar = models.ImageField(upload_to='atavar/', blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'Usuário: {self.username}'


class Noticia(models.Model):
    TIPOS_ESCOLHAS = (
        ('P', 'Pública'),
        ('A', 'Assinante'),
        ('H', 'Híbrida')
    )

    titulo = models.CharField(max_length=150, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    tipo = models.CharField(choices=TIPOS_ESCOLHAS, max_length=1, verbose_name='Tipo')
    foto = models.ImageField(upload_to='noticia/', blank=True)

    class Meta:

        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo
    
    def save(self):
        super().save()
        redimensionar(self.foto.path)
        adicionar_marca_dagua(self.foto.path)
        aplicar_tons_verde(self.foto.path)


class Servico(models.Model):
    VALIDADE_SERVICO = (
        (0, 6),
        (1, 15),
        (2, 30)
    )

    nome = models.CharField(max_length=50, verbose_name='Nome do serviço')
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preço do serviço')
    descricao = models.TextField(verbose_name='Descrição do serviço')
    validade = models.IntegerField(choices=VALIDADE_SERVICO, default=0)

    class Meta:

        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return f'{self.nome} - {self.preco}'
