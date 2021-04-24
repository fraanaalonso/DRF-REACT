from django.contrib import admin
from posts.models import Category, Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', 'author')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )



