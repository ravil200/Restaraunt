from django.contrib import admin
from django.contrib.admin import ModelAdmin, register


from .models import Category, Post, Comment

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('category_name',)

@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'content', 'author', 'image', 'category', 'created',)

@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('user', 'post', 'content', 'created',)

# Register your models here.
