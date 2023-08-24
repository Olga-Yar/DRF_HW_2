
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Subscription(models.Model):
    is_sub = models.BooleanField(default=True, verbose_name='подписан')
    course = models.ManyToManyField('Course', verbose_name='курс', **NULLABLE)

    def __str__(self):
        return f'{self.course}: {self.is_sub}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
