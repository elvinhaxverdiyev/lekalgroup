from django.db import models
from utils.az_slugify import az_slugify


class Category(models.Model):
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Əsas kateqoriya'
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Ad'
    )
    slug = models.SlugField(
        verbose_name='Slug',
        editable=False,
        unique=True,
        null=True,
        blank=True 
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = f'{az_slugify(self.name)}-{self.id}'
            super().save(update_fields=['slug'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
    