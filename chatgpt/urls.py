from django.urls import path
from chatgpt import views

urlpatterns = [
    path('',views.main_page, name='main_page' ),
    path('chatting',views.chatting_page, name='chatting_page' ),

]