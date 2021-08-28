from django.contrib import admin

from account.models import Account


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'type_user',]


admin.site.register(Account, AccountModelAdmin)

