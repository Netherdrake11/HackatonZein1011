from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlockedIP


@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'blocked_until', 'is_blocked')
    list_filter = ('blocked_until',)
    actions = ['unblock_selected_ips']

    def unblock_selected_ips(self, request, queryset):
        for blocked_ip in queryset:
            blocked_ip.delete()
        self.message_user(request, "Выбранные IP-адреса разблокированы.")

    unblock_selected_ips.short_description = "Разблокировать выбранные IP"
