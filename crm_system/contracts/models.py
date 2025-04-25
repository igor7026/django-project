from django.db import models

# Create your models here.


class Contract(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Конец')
    product = models.ForeignKey('products.Product', on_delete=models.SET('Услуга удалена'), verbose_name='Услуга')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    document = models.FileField(upload_to='contracts/', blank=True, null=True, verbose_name='Документ')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракты'
        ordering = ['name']

    def __str__(self):
        return self.name
    