from django.contrib import admin
from .models import Developer, User


class ApiUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'code', 'created_at')
    readonly_fields = ('created_at', 'code')


class UserAdmin(admin.ModelAdmin):
    list_filter = ('created_by', )
    list_display = ('username', 'first_name', 'second_name', 'created_at', 'created_by')
    readonly_fields = ('created_at', 'created_by')


admin.site.register(User, UserAdmin)
admin.site.register(Developer, ApiUserAdmin)