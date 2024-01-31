from django.db import models
from usuario.models import Cliente

from uuid import uuid4


class HistoryQuestion(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sender = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    message = models.TextField()
    date_only = models.DateField(auto_now_add=True)
    time_only = models.TimeField(auto_now_add=True)
    

class Conversation(models.Model):
    user_question = models.TextField()
    bot_response = models.TextField()
    date_only = models.DateField(auto_now_add=True)
    time_only = models.TimeField(auto_now_add=True)
    is_first_message = models.BooleanField(default=False)
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    chat_message = models.ForeignKey(HistoryQuestion, on_delete=models.CASCADE)


class UploadedFile(models.Model):
    file_name = models.CharField(max_length=200, null=True)
    file_url = models.URLField(null=True)
    user = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

