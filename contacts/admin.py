from django.contrib import admin
from .models import Contact

class contactAdmin(admin.ModelAdmin):
    list_display = ('id','acronym','user_name')
    search_fields = ('acronym',)


admin.site.register(Contact, contactAdmin)
