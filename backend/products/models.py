from django.db import models

"""
Create Product Model:
- title
- content
- price
"""
class Product(models.Model):
    title=models.CharField(max_length=120)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, default=0.0, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
    
    def get_discount(self):
        return "123"
    def get_promotion(self):
        return '200'