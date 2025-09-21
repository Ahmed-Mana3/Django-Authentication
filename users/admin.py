from django.contrib import admin
from .models import ModUsers, BanedUsers


admin.site.register(ModUsers)
admin.site.register(BanedUsers)
