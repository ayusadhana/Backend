from django.db import models
import uuid


class Products(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    product_name = models.CharField(max_length=255, null=False, default='Default Product Name')
    image_path = models.CharField(max_length=255)
    product_description = models.TextField()
    quantity = models.IntegerField(default=1)
    formulation = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
