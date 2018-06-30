from django.urls import path
from . import views


app_name ="diary"
urlpatterns = [
    path('', views.question.as_view(), name='question'),
    path('startchat/', views.start_chat.as_view(), name='startchat'),
]