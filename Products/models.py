from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    weight = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'