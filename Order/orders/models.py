from django.db import models
from django.utils.text import slugify
# from Order.autsh import User

class Order(models.Model):

    user = models.IntegerField()
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    order_shipped = models.BooleanField(default=False)
    order_quantity = models.PositiveIntegerField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)  

    def save(self, *args, **kwargs):
        self.slug = str(self.id)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order for {self.user} - ${self.order_value}"
