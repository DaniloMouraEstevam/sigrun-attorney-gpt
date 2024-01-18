from django.urls import path
from . import views
from .views import edit_profile

app_name= 'chat'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('user/', views.user, name = 'user'),
    path('user/edit/', edit_profile, name='edit_profile'),
]