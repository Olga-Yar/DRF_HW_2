from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Lesson


class LessonTestCase(APITestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(
            name='test_test',
            about='test_about_test',
            url='https://youtube.com/watch'
        )

    def test_get_list(self):
        """Тест для получения списка уроков"""

        response = self.client.get(
            reverse('main:lesson_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

