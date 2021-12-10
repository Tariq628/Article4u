from django.contrib import admin
from .models import addPost
from django_summernote.admin import SummernoteModelAdmin
# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()
# Register your models here.
@admin.register(addPost)
class addPostAdmin(SummernoteModelAdmin):
    list_display = ["postId", "title", "category"]