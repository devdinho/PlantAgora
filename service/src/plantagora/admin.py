from django.contrib import admin

from plantagora.models import (BaseAddress, Garden, GardenAddress, GardenBed,
                               Grower, Signature)


class GardenAddressInline(admin.TabularInline):
    model = GardenAddress
    extra = 0
    fields = ("street", "number", "zip_code", "city")
    show_change_link = True
    icon_name = "home"
    autocomplete_fields = ("city",)


class GardenAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "status")
    search_fields = ("name", "code")
    list_filter = ("status",)
    readonly_fields = ("code",)
    icon_name = "local_florist"
    inlines = [GardenAddressInline]


class GardenAddressAdmin(admin.ModelAdmin):
    list_display = (
        "street",
        "number",
        "zip_code",
        "city",
        "garden",
        "status",
    )
    search_fields = ("id", "street", "number", "zip_code")
    list_filter = ("city", "garden")
    icon_name = "home"
    autocomplete_fields = (
        "garden",
        "city",
    )


class GrowerAdmin(admin.ModelAdmin):
    list_display = (
        "profile",
        "document",
        "documentType",
    )
    search_fields = (
        "profile",
        "document",
    )
    autocomplete_fields = (
        "profile",
        "address",
    )
    icon_name = "person"


class BaseAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "street",
        "number",
        "zip_code",
        "city",
    )
    list_display_links = (
        "id",
        "street",
        "number",
        "zip_code",
        "city",
    )
    search_fields = ("id", "street", "number", "zip_code")
    list_filter = ("city",)
    icon_name = "home"
    autocomplete_fields = ("city",)


class SignatureAdmin(admin.ModelAdmin):
    list_display = ("garden", "grower", "status", "releasedAt", "updatedAt")
    search_fields = ("garden", "grower")
    list_filter = ("garden", "status")
    readonly_fields = ("updatedAt",)
    autocomplete_fields = ("grower", "garden")
    icon_name = "assignment"


class GardenBedAdmin(admin.ModelAdmin):
    list_display = ("code", "garden", "signature")
    search_fields = ("code",)
    list_filter = ("garden", "signature")
    readonly_fields = ("code",)
    autocomplete_fields = ("garden", "signature", "garden_address")
    icon_name = "view_module"


admin.site.register(Garden, GardenAdmin)
admin.site.register(GardenAddress, GardenAddressAdmin)
admin.site.register(BaseAddress, BaseAddressAdmin)
admin.site.register(Grower, GrowerAdmin)
admin.site.register(Signature, SignatureAdmin)
admin.site.register(GardenBed, GardenBedAdmin)
