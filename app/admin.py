from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')  # Add 'created_at' to list_display
    list_filter = ('created_at',)  # Add 'created_at' to list_filter

admin.site.register(Contact, ContactAdmin)
