from django.db import models
from usuario.models import Cliente


class HistoryQuestion(models.Model):
    sender = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date_only = models.DateField(auto_now_add=True)
    


class Conversation(models.Model):
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    chat_message = models.ForeignKey(HistoryQuestion, on_delete=models.CASCADE)
    user_question = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_first_message = models.BooleanField(default=False)

