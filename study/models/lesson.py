from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='Course/', verbose_name='превью', **NULLABLE)
    about = models.TextField(verbose_name='описание', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ManyToManyField('Course', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
