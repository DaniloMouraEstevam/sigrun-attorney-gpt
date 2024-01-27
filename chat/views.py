from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from usuario import models as usuario
from chat import models as chat
from .forms import EditProfileForm

from datetime import timedelta
from dotenv import load_dotenv

import json
import openai


# load_dotenv()
# openai.api_key = settings.OPEN_API_KEY


# def ask_openai(message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )

#     return response['choices'][0]['message']['content']


@login_required(login_url='usuario:login')
def home(request):
    today = timezone.now().date()
    seven_days_ago = today - timedelta(days=7)
    thirty_days_ago = today - timedelta(days=30)

    questions = chat.HistoryQuestion.objects.filter(sender=request.user)
    t_questions = questions.filter(date_only=today)
    s_questions = questions.filter(date_only__range=(seven_days_ago, today))
    td_questions = questions.filter(date_only__range=(thirty_days_ago, seven_days_ago))
    
    context = {"t_questions": t_questions, "s_questions": s_questions, "td_questions": td_questions}
    
    # Verifica se a requisição é AJAX
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        data = [{"message": tq.message} for tq in t_questions]
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'gpt.html', context)


@login_required(login_url='usuario:login')
def get_question(request):
    data = json.loads(request.body)
    message = data.get("msg", "")
    current_chat_id = data.get("chat_message_id")
    response = 'teste'  # response = ask_openai(message)

    if data.get('is_first_message', False):
        history_question = chat.HistoryQuestion.objects.create(sender=request.user, message=message)
        request.session['history_question_id'] = history_question.id
        first_id = history_question.id
        chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response, is_first_message=True)
    else:
        history_question_id = request.session.get('history_question_id')
        first_id = None

        if current_chat_id is not None:
            old_question = get_object_or_404(chat.HistoryQuestion, id=current_chat_id)
            chat.Conversation.objects.create(user=request.user, chat_message=old_question, user_question=message, bot_response=response)
        elif history_question_id is not None:
            history_question = get_object_or_404(chat.HistoryQuestion, id=history_question_id)
            chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response)
    
    return JsonResponse({'msg': message, 'res': response, 'first_id': first_id})


@login_required(login_url='usuario:login')
def view_messages(request, chat_message_id):
    messages = chat.Conversation.objects.filter(chat_message__id=chat_message_id)

    data = [{'user_question': message.user_question, 'bot_response': message.bot_response} for message in messages]

    return JsonResponse(data, safe=False)



    

# def home(request):
    # cliente_username = request.user.username

    # try:
    #     cliente_logado = usuario.Cliente.objects.get(username=cliente_username)
    # except usuario.Cliente.DoesNotExist:
    #     cliente_logado = None

    # return render(request, 'chat.html', {'cliente_logado': cliente_logado})


# def user(request):
#     return render(request, 'user.html')


# def edit_profile(request):
#     user = request.user

#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, request.FILES, instance=user)

#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Perfil atualizado com sucesso!')
#             return redirect('chat:user')
#         else:
#             messages.error(
#                 request, 'Erro ao atualizar o perfil. Por favor, corrija os erros abaixo.')
#     else:
#         form = EditProfileForm(instance=user)

#     return render(request, 'user.html', {'form': form})
