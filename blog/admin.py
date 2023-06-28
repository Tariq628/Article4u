from django.contrib import admin
from .models import addPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(addPost)
class addPostAdmin(SummernoteModelAdmin):
    list_display = ["postId", "title", "category"]
