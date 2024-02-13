from django.contrib import admin
from .models import Contact, FreeColor, UserDefCategory, Task

class contactAdmin(admin.ModelAdmin):
    list_display = ('acronym','user_name')
    search_fields = ('acronym',)

class taskAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'author', 'column')
    search_fields = ('title', 'priority')

class UserDefCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')

admin.site.register(Contact, contactAdmin)
admin.site.register(Task, taskAdmin)
admin.site.register(UserDefCategory, UserDefCategoryAdmin)
admin.site.register(FreeColor)
