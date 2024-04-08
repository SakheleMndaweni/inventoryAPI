from django.db import models


class Inventory(models.Model):
        quantity = models.IntegerField()
        itemCode = models.CharField(max_length=255, null=True)
        # returns the order id as a string
        def __str__(self):
            return str(itemCode)
