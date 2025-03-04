from django.db import models
from django.contrib.auth.models import User

class BlogModels(models.Model):
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to="media")
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post", blank=True)

    def __str__(self):
        return self.title
