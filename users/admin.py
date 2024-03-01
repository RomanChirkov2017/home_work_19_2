from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'country', 'email_verified',)
    list_filter = ('country', 'email_verified',)
    search_fields = ('last_name', 'email', 'country', 'email_verified')
