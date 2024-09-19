from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Article

class ArticleAdmin(ModelAdmin):
    search_fields = ['title', ]
    list_display = ['author', 'title', 'is_display', 'is_index', ]
    list_filter = ['is_display', 'is_index', ]
    list_editable = ['is_display', 'is_index', ]

admin.site.register(Article, ArticleAdmin)
# Register your models here.
