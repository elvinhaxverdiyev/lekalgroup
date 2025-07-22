from django.db import models
from .product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Məhsul',
        null=True,
        blank=True 
    )
    image = models.ImageField(
        upload_to='product_images',
        verbose_name='Məhsul şəkli',
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Image#{self.id} of {self.product.name}'
    
    class Meta:
        verbose_name = 'Məhsul şəkli'
        verbose_name_plural = 'Məhsul şəkilləri'
    