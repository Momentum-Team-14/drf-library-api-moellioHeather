from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Book, List, MarkUp, Genre

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(List)
admin.site.register(MarkUp)
admin.site.register(Genre)
