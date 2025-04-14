from django.contrib import admin

from utils.models import City, State

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name',)
    list_filter = ('state',)
    icon_name = 'location_city'
    autocomplete_fields = ('state',)
    
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')
    search_fields = ('name',)
    list_filter = ('abbreviation',)
    icon_name = 'map'
    
    
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)