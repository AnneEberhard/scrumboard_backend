from django.contrib import admin
from .models import Task

class taskAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'author', 'column')
    search_fields = ('title', 'priority')

admin.site.register(Task, taskAdmin)
