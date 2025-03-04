from django.db import models

from organiqueFood.models import ProductsFilter
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="category")

    def __str__(self):
        return self.name

class Product(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    desctptions = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Items", blank=False)
    category = models.ForeignKey(Category, related_name="kinds", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=2000, blank=False, null=False, decimal_places=2)
    discount = models.DecimalField(max_digits=2000, blank=True, null=True, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    still_available = models.BooleanField(default=True)
    filters = models.ManyToManyField(ProductsFilter, related_name="filter", blank=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.name} {self.price}Ar"

    def is_liked(self):
        return self.likes.filter(id=self.poster.id)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now
