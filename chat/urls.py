from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('get-question/', views.get_question, name='get_question'),
    path('view-messages/<int:chat_message_id>', views.view_messages, name='view_messages'),
]
