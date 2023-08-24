from rest_framework import serializers

from study.models import Lesson
from study.validators import validator_scam_url


class LessonBaseSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[validator_scam_url])

    class Meta:
        model = Lesson
        fields = [
            'name', 'about', 'url', 'image',
        ]
