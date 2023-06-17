from django.contrib import admin

from .models import Mycontacts

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lisiting', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'lisiting')
    list_per_page = 25


admin.site.register(Mycontacts, ContactAdmin)
