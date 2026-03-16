from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def getName(self):
        return self.name

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"

class WaterBottle(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    mouth_size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()

    def __str__(self):
        return (f"{self.sku}: {self.brand}, {self.mouth_size}, "
                f"{self.size}, {self.color}, supplied by "
                f"{self.supplier.name}, {self.cost} : {self.current_quantity}")
