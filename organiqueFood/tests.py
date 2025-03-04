from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from mediamodels.models import Product

class ProductModelTest(TestCase):
    def test_was_published_recently_with_future_product(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futur_product = Product(created=time)

        self.assertIs(futur_product.was_published_recently(), False)