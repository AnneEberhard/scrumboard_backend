from django.contrib import admin
from .models import Subtask


class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(Subtask)