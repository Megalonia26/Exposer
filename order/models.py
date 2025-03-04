from django.db import models
from django.contrib.auth.models import User
from mediamodels.models import Product

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item}"