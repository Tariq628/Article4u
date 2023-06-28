from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    image = models.ImageField(upload_to="blog/images", default="")
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "id"

    def __str__(self):
        return self.title
