from django.conf import settings
from django.shortcuts import render, redirect
from usuario import models as usuario
from .forms import EditProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models.functions import TruncDate

from chat import models as chat

from datetime import timedelta
from dotenv import load_dotenv

from django.contrib.auth.decorators import login_required

import json
import openai


load_dotenv()
# openai.api_key = settings.OPEN_API_KEY


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    return response['choices'][0]['message']['content']


@login_required(login_url='usuario:login')
def home(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    thirty_days_ago = today - timedelta(days=30)

    questions = chat.HistoryQuestion.objects.filter(sender=request.user)
    t_questions = questions.filter(date_only=today)
    s_questions = questions.filter(date_only__gte=seven_days_ago, date_only__lt=today)
    td_questions = questions.filter(date_only__gte=thirty_days_ago, date_only__lt=today)
    
    context = {"t_questions": t_questions, "s_questions": s_questions, "td_questions": td_questions}
    
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Se for uma solicitação AJAX, retorne JSON
        data = [
            {"message": tq.message} for tq in t_questions
        ]  # Ajuste conforme necessário
        return JsonResponse(data, safe=False)
    else:
        # Se não for uma solicitação AJAX, renderize o template normalmente
        return render(request, 'gpt.html', context)
    # cliente_username = request.user.username

    # try:
    #     cliente_logado = usuario.Cliente.objects.get(username=cliente_username)
    # except usuario.Cliente.DoesNotExist:
    #     cliente_logado = None

    # return render(request, 'chat.html', {'cliente_logado': cliente_logado})


@login_required(login_url='usuario:login')
def get_question(request):
    data = json.loads(request.body)
    message = data["msg"]
    # response = ask_openai(message)
    response = 'teste'

    if data.get('is_first_message', False):
        history_question = chat.HistoryQuestion.objects.create(sender=request.user, message=message)
        request.session['history_question_id'] = history_question.id
        chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response, is_first_message=True)
    else:
        history_question_id = request.session.get('history_question_id')
        if history_question_id is not None:
            history_question = chat.HistoryQuestion.objects.get(id=history_question_id)
            chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response)
    
    return JsonResponse({'msg': message, 'res': response})


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
            messages.error(
                request, 'Erro ao atualizar o perfil. Por favor, corrija os erros abaixo.')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'user.html', {'form': form})
