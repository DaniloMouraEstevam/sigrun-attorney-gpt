from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from attorney_gpt.storage_azure import upload_file_to_blob
from usuario import models as usuario
from chat import models as chat
from .forms import EditProfileForm

from datetime import timedelta
from dotenv import load_dotenv

import base64
import json
import openai
import os

load_dotenv()

STORAGE_KEY = settings.AZURE_STORAGE_KEY
STORAGE_DOMAIN = settings.AZURE_STORAGE_DOMAIN
STORAGE_CONTAINER = settings.AZURE_MEDIA_CONTAINER

DATA_KEY = settings.AZURE_DATA_KEY
DATA_DOMAIN = settings.AZURE_DATA_DOMAIN
DATA_DOC_CONTAINER = settings.AZURE_DOC_CONTAINER
DATA_IMG_CONTAINER = settings.AZURE_IMG_CONTAINER

def handle_file(file, key, domain, container, user, conversation):
    filename = file.name
    base_name, extension = os.path.splitext(filename)
    
    params = {
        'file': filename,
        'key': key,
        'domain': domain,
        'container': container
    }
    upload_params = {
        'file': file,
        'filename': base_name,
        'extension': extension,
        'params': params
    }
    
    file_url = upload_file_to_blob(**upload_params)
    
    if file_url is not None:
        file_content = base64.b64encode(file.read()).decode('utf-8')

        result = {
            'file_name': base_name,
            'file_url': file_url,
            'file_content': file_content
        }

        chat.UploadedFile.objects.create(file_name=base_name, file_url=file_url, user=user, conversation=conversation)

        return result
    
    return None

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
    yesterday = today - timedelta(days=1)
    seven_days_ago = today - timedelta(days=7)
    thirty_days_ago = today - timedelta(days=30)
    
    questions = chat.HistoryQuestion.objects.filter(sender=request.user).order_by('-time_only')
    # file = chat.UploadedFile.objects.filter(file_name='187 APTO 45 NOV').first()

    t_questions = questions.filter(date_only=today)
    s_questions = questions.filter(date_only__range=(seven_days_ago, yesterday))
    td_questions = questions.filter(date_only__range=(thirty_days_ago, seven_days_ago))

    context = {'t_questions': t_questions, 's_questions': s_questions, 'td_questions': td_questions}
    
    # Verifica se a requisição é AJAX
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        data = [{'message': tq.message, 'time': tq.time_only } for tq in t_questions]
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'gpt.html', context)


@login_required(login_url='usuario:login')
def get_question(request):
    if request.method == 'POST':
        is_first_message = request.POST.get("is_first_message")
        message = request.POST.get("msg", "")
        current_chat_id = request.POST.get("chat_message_id")
        response = 'teste'  # response = ask_openai(message)
        document_file = request.FILES.get('document')
        image_file = request.FILES.get('image')

        
        if is_first_message == 'true':
            
            history_question = chat.HistoryQuestion.objects.create(sender=request.user, message=message)
            
            request.session['history_question_id'] = history_question.id
            first_id = history_question.id
            time = history_question.time_only
            

            chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response, is_first_message=True)
        else:
            
            history_question_id = request.session.get('history_question_id')
            first_id = None

            if current_chat_id is not None and current_chat_id != 'undefined':
                old_question = get_object_or_404(chat.HistoryQuestion, id=current_chat_id)
                chat.Conversation.objects.create(user=request.user, chat_message=old_question, user_question=message, bot_response=response)
                time = old_question.time_only
            elif history_question_id is not None:
                history_question = get_object_or_404(chat.HistoryQuestion, id=history_question_id)
                chat.Conversation.objects.create(user=request.user, chat_message=history_question, user_question=message, bot_response=response)
                time = history_question.time_only
            
        
        last_conversation = chat.Conversation.objects.last()
        uploaded_files = []

        if document_file:
            result_document = handle_file(document_file, DATA_KEY, DATA_DOMAIN, DATA_DOC_CONTAINER, request.user, last_conversation)
            result_document['type'] = 'text'
            if result_document:
                uploaded_files.append(result_document)
        
        if image_file:
            result_document = handle_file(image_file, DATA_KEY, DATA_DOMAIN, DATA_IMG_CONTAINER, request.user, last_conversation)
            result_document['type'] = 'image'
            if result_document:
                uploaded_files.append(result_document)
        
        
        
        return JsonResponse({'msg': message, 'res': response, 'time': time, 'first_id': first_id, 'files': uploaded_files})


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
