from django import forms
from usuario.models import Cliente

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password', 'oab', 'foto_perfil']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
        return password
