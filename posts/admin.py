from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class addPostAdmin(SummernoteModelAdmin):
    list_display = ["id", "title", "category"]
