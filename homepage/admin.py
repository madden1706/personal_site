from django.contrib import admin
from blog.models import SeoKeyword, BlogPost

# Register your models here.

admin.site.unregister(BlogPost)


class SeoKeywordInLine(admin.TabularInline):
    model = SeoKeyword


class BlogPostAdmin(admin.ModelAdmin):
    #fieldsets = []
    inlines = [SeoKeywordInLine]


admin.site.register(BlogPost, BlogPostAdmin)

