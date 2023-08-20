from django.contrib.auth import get_user_model
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Payments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    payment_sum = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user}: {self.payment_sum}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
