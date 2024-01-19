from django import forms
from usuario.models import Cliente

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'oab', 'foto_perfil']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password and len(password) < 8:
            raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
        return password
