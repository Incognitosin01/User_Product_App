from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='Product Name',help_text="Please keep product name between 200 characters")
    weight = models.FloatField(verbose_name='Product Weight')
    price = models.DecimalField(verbose_name='Product Price',max_digits=8,decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"