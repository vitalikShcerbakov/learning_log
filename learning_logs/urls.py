from argparse import Namespace
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/', views.topics, name='topics'),
    path('<int:topic_id>/', views.topic, name='topic'),
    #url(r'^new_topic/$', views.new_topic, name='new_topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:id>', views.new_entry, name='new_entry'),
]