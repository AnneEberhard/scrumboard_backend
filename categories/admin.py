from django.contrib import admin
from .models import UserDefCategory

class UserDefCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'colorCode')

admin.site.register(UserDefCategory, UserDefCategoryAdmin)