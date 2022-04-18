from django.contrib import admin
from django.contrib.admin import ModelAdmin, register


from .models import Category, Meals

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)

@register(Meals)
class MealsAdmin(ModelAdmin):
    list_display = ('name', 'description', 'category', 'people',
     'is_specionality', 'price', 'image', 'preparation_time', 'slug',)