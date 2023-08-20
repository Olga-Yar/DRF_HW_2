from rest_framework import serializers

from study.models import Lesson


class LessonBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'name', 'about', 'url', 'image',
        ]
