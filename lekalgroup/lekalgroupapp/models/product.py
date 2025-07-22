from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Kateqoriya'
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Ad'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Haqqında'
    )
    price = models.FloatField(
        verbose_name='Qiymət'   
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Məhsul aktivliyi'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'
    
   