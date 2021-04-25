from django.contrib import admin
from posts.models import Category, Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('uid', 'title', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', )



