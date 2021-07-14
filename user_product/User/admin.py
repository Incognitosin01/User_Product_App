from .models import Post
from django.contrib import admin

# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['user','created_at','updated_at']
    search_fields = ['created_at','updated_at']
    raw_id_fields = ['user']
    