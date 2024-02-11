from django.contrib import admin
from .models import CustomUser, UserDefCategory, Task

class userAdmin(admin.ModelAdmin):
    list_display = ('username','first_name',  'last_name')
    search_fields = ('acronym',)

class taskAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'author','title',  'column_category')
    search_fields = ('title', 'priority')

admin.site.register(CustomUser, userAdmin)
admin.site.register(Task, taskAdmin)
admin.site.register(UserDefCategory)
