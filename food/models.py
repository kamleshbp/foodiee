from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.FloatField()
    item_image = models.CharField(max_length=500, default='https://www.dirtyapronrecipes.com/wp-content/uploads/2015/10/food-placeholder.png')
    item_created_by = models.ForeignKey(User, on_delete= models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})

