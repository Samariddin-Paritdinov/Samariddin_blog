from django.contrib import admin

from .models import  Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner__username', 'created_at', 'updated_at',)
    list_display_links = ('id', 'title', 'owner__username',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'description',)
    readonly_fields = ('views_count',)
