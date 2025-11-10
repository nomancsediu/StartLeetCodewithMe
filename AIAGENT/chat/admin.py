from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user_message', 'timestamp']
    list_filter = ['timestamp']
    readonly_fields = ['timestamp']