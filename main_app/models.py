from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

CATEGORIES = (
    ( "bed", "Bed"),
    ("chair", "Chair"),
    ("sofa", "Sofa"),
    ("table", "Table")
)

class Furniture_Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    category = models.CharField(choices=CATEGORIES)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
       
        return reverse("detail", kwargs={"furniture_item_id": self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    furniture_item = models.ForeignKey(Furniture_Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for furniture_item_id: {self.furniture_item_id} @{self.url}"
    
class Cart(models.Model):
    furniture_item = models.ManyToManyField(Furniture_Item, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

