from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'relative_url', 'full_url')
    search_fields = ('title', 'parent')
    list_filter = ('parent',)

admin.site.register(Menu, MenuAdmin)
