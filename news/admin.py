from django.contrib import admin
from .models import BlogNews

# Register your models here.

# from .models import BlogNews

# admin.site.register(BlogNews)
@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    list_display = ("blog_name", "category", "count_views")
    readonly_fields = ("count_views", )