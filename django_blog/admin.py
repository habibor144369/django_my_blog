from django.contrib import admin
from .models import Author, Category, Article, About_Me

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['title', 'artcle_author', 'published', 'slug', 'category', 'unique_id']
    list_per_page = 10
    search_fields = ['title']
    list_filter = ['title', 'published', 'category']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article, PersonAdmin)
admin.site.register(About_Me)