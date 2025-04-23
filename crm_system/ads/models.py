from itertools import product
from django.db import models

# Create your models here.

class Ads(models.Model):

    name = models.CharField(max_length=255, verbose_name='Рекламная кампания')
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Бюджет')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Услуга')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    
