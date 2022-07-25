from django.contrib import admin
from learning_logs.models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
"""Этот код импортирует модель Topic , после чего использует вызов admin.site.
register() , регистрирующий модель для управления через административный
сайт.
"""
# Register your models here.

