from django.contrib import admin
from .models import Subtask, UserDefCategory, Task



class taskAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'author', 'column')
    search_fields = ('title', 'priority')

class UserDefCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'colorCode')

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id','description')


admin.site.register(Task, taskAdmin)
admin.site.register(UserDefCategory, UserDefCategoryAdmin)
admin.site.register(Subtask)
