from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    is_point_extra_service = models.BooleanField()

    def __str__(self):
        return self.name

class SalesCampaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    charge = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop")

    def __str__(self):
        return self.name + "-" + str(self.charge)
    