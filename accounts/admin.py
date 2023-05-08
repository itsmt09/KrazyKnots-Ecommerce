from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Account

#makes password field to read only in admin [anel]
class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('first_name', "last_name", 'username', 'email')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(Account, AccountAdmin)
