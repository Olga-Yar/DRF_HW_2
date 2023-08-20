from rest_framework import serializers

from study.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name',)


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [i.pk for i in obj.lessons.all()]

    class Meta:
        model = Course
        fields = ('name', 'about', 'count_lessons')
