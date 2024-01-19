from django.shortcuts import render, redirect
from usuario import models as usuario
from .forms import EditProfileForm
from django.contrib import messages

def home(request):
    
    cliente_username = request.user.username

    try:
        cliente_logado = usuario.Cliente.objects.get(username=cliente_username)
    except usuario.Cliente.DoesNotExist:
        cliente_logado = None
    
    return render(request, 'chat.html', {'cliente_logado': cliente_logado})


def user(request):
    return render(request, 'user.html')

def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('chat:user')
        else:
            messages.error(request, 'Erro ao atualizar o perfil. Por favor, corrija os erros abaixo.')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'user.html', {'form': form})