from django.urls import re_path,include,path
from . import views

urlpatterns =[
    path('',views.send_message,name='message'),
    re_path(r'^reply/$',views.message_sent,name='sent_message'),

]