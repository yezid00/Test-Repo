
from django.contrib import admin
from django.contrib.auth.models import Group

from project.accounts.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = [
        'email',
        'is_active'
    ]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

