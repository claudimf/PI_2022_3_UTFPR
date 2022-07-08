from django.contrib.auth import forms
from django import forms as models_form
from easy_select2.widgets import Select2, Select2Multiple

from .models import User, Noticia, Servico


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fieldsets = (
            ('Informações do Usuário', {
                'fields': (
                    'avatar',
                ),
            }),
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.is_staff = True

        if commit:
            user.save()

        return user


class SignUpForm(UserCreationForm):
    email = models_form.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')


class NoticiaForm(models_form.ModelForm):
    class Meta:

        model = Noticia
        fields = '__all__'


class ServicoForm(models_form.ModelForm):
    class Meta:

        model = Servico
        fields = '__all__'
