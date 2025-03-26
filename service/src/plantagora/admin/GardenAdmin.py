from django.contrib import admin

from plantagora.models import Garden
class GardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status')
    search_fields = ('name', 'code')
    list_filter = ('status',)
    readonly_fields = ('code',)
    icon_name = 'local_florist'
    
admin.site.register(Garden,GardenAdmin)