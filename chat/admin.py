from django.contrib import admin

# Register your models here.
from chat.models import Chat, Jobs, Qualified


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('message', 'created', 'user',)
    search_fields = ['message']


admin.site.register(Jobs)
admin.site.register(Qualified)