from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('get-question/', views.get_question, name='get_question'),
    path('user/', views.user, name='user'),
    path('user/edit/', views.edit_profile, name='edit_profile'),
]
