from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from easy_select2 import select2_modelform


from .forms import UserChangeForm, UserCreationForm
from .models import User, Noticia, Servico


@admin.register(User)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = ("Informações do Usuário", {"fields": ("username", "email", "avatar",)}),


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    form = select2_modelform(Noticia)
    list_display = ("titulo", "tipo",)
    search_fields = ("titulo", "tipo")
    ordering = ("tipo",)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    '''Admin View for Servico'''

    form = select2_modelform(Servico)
    list_display = ("nome", "preco",)
    search_fields = ("nome", )
    ordering = ("nome",)
