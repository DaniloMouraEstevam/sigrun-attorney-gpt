from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from usuario import models


def login_form(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('confirm_senha')
        oab = request.POST.get('oab')

        status_messages = {}

        try:
            if not nome.strip() or not email.strip():
                raise ValueError('Nome e email não podem estar vazios.')

            if len(senha) < 8:
                raise ValueError('A senha deve ter no mínimo 8 caracteres.')

            if not senha == conf_senha:
                raise ValueError('As senhas não coincidem')

            if models.Cliente.objects.filter(email=email).exists():
                raise ValueError('Email já cadastrado.')

            usuario = models.Cliente(username=nome, email=email, oab=oab)
            usuario.set_password(senha)  # Set the hashed password
            usuario.save()

            status_messages = {'class': 'bg-success text-white',
                               'message': 'Usuário cadastrado com sucesso!!'}
            return render(request, 'cadastro.html', {'status_messages': status_messages})

        except ValueError as error:
            error_message = str(error)
            status_messages = {
                'class': 'bg-danger text-white', 'message': error_message}
            return render(request, 'cadastro.html', {'status_messages': status_messages})


def valida_login(request):
    # if request.user.is_authenticated:
    #     return redirect('chat:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        try:
            # Use a função authenticate para verificar as credenciais
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                # Usuário autenticado com sucesso
                login(request, user)  # Faça login no usuário
                return redirect('chat:home')

            else:
                # Credenciais inválidas
                status_message = {'class': 'bg-danger text-white',
                                  'message': 'Email ou senha incorretos.'}
                return render(request, 'login.html', {'status_messages': status_message})

        except Exception as e:
            status_message = {'class': 'bg-danger text-white',
                              'message': f'Erro interno: {str(e)}'}
            return render(request, 'login.html', {'status_messages': status_message})


def sair(request):
    logout(request)
    return redirect('index')
