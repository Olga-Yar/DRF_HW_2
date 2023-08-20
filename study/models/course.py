from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='Course/', verbose_name='превью', **NULLABLE)
    about = models.TextField(verbose_name='описание', **NULLABLE)

    student = models.ManyToManyField('users.User', verbose_name='студент', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
