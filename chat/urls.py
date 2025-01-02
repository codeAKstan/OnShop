from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    path('', lambda request: redirect('/chat/default/')),  # Redirect /chat/ to a default room
]
