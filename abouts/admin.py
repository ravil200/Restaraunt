from django.contrib import admin
from django.contrib.admin import ModelAdmin, register


from .models import AboutUs, WhyChoiceUs, Chef

@register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    list_display = ('title', 'content', 'image',)

@register(WhyChoiceUs)
class WhyChoiceUsAdmin(ModelAdmin):
    list_display = ('title', 'content',)

@register(Chef)
class ChefAdmin(ModelAdmin):
    list_display = ('name', 'subtitle', 'bio', 'image',)