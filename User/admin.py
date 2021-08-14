from django.contrib import admin
from .models import Post,Users

admin.site.register(Users)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']

admin.site.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['user','text']