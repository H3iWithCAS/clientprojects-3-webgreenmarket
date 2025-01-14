from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField() 
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
