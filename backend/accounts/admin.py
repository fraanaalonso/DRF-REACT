from django.contrib import admin
from accounts.models import User
# Register your models here.

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uid', 'user_name', 'email')



