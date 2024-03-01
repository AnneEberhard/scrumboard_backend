from django.contrib import admin
from .models import Subtask, Task



class taskAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'author', 'column')
    search_fields = ('title', 'priority')



class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id','description')


admin.site.register(Task, taskAdmin)

admin.site.register(Subtask)
