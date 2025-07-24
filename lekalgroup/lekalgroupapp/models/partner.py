from django.db import models


class Partner(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Ad'
    )

    logo = models.ImageField(
        upload_to='logo_images/',
        verbose_name='Əməkdaş logo şəkli',
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Əməkdaş aktivliyi'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Əməkdaş'
        verbose_name_plural = 'Əməkdaşlar'
    