from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "price", "status",)
    list_filter = ("status",)
    search_fields = ("meal", "description",)


admin.site.register(Item, ItemAdmin)