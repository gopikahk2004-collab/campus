from django.contrib import admin
from .models import MaintenanceRequest

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'status', 'user', 'date_reported')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description', 'location')
