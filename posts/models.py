from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    RANDOM_FACTS = 'random_facts'
    TECHNOLOGY = 'technology'
    SPORTS = 'sports'
    POETS = 'poets'

    CATEGORY_CHOICES = [
        (RANDOM_FACTS, 'Random Facts'),
        (TECHNOLOGY, 'Technology'),
        (SPORTS, 'Sports'),
        (POETS, 'Poets'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="blog/images")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        get_latest_by = "id"

    def __str__(self):
        return self.title
