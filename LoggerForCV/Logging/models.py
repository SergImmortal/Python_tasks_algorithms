from django.db import models


# Create your models here.
class Logging(models.Model):
    ip = models.CharField(max_length = 255, verbose_name='Ip адрес')
    referrer = models.CharField(max_length = 255, verbose_name='Referrer')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True,  blank=True, editable=True)

    class Meta:
        verbose_name = 'Referrer'
        verbose_name_plural = 'Referrers'