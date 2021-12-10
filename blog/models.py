from django.db import models
from datetime import datetime
# Create your models here.
class addPost(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    image = models.ImageField(upload_to="blog/images", default="")
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = "date"
    def __str__(self):
        return self.title