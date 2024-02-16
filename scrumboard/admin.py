from django.contrib import admin
from .models import Contact, FreeColor, Subtask, UserDefCategory, Task

class contactAdmin(admin.ModelAdmin):
    list_display = ('id','acronym','user_name')
    search_fields = ('acronym',)

class taskAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at', 'author', 'column')
    search_fields = ('title', 'priority')

class UserDefCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'colorCode')

class FreeColorAdmin(admin.ModelAdmin):
    list_display = ('freeColorCode')

class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(Contact, contactAdmin)
admin.site.register(Task, taskAdmin)
admin.site.register(UserDefCategory, UserDefCategoryAdmin)
admin.site.register(FreeColor)
admin.site.register(Subtask)
