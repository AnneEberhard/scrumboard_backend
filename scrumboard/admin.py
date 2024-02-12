from django.contrib import admin
from .models import Contact, UserDefCategory, Task

class contactAdmin(admin.ModelAdmin):
    list_display = ('acronym','first_name',  'last_name')
    search_fields = ('acronym',)

class taskAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'author','title',  'column_category')
    search_fields = ('title', 'priority')

admin.site.register(Contact, contactAdmin)
admin.site.register(Task, taskAdmin)
admin.site.register(UserDefCategory)
