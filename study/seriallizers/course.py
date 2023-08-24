from rest_framework import serializers

from study.models import Course
from study.seriallizers.subscription import SubBaseSerializer


class CourseSerializer(serializers.ModelSerializer):
    is_sub = serializers.SerializerMethodField()
    count_lessons = serializers.SerializerMethodField()
    lesson = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [i.pk for i in obj.lessons.all()]

    class Meta:
        model = Course
        fields = ('name', 'about', 'count_lessons', 'is_sub')

# class CourseListSerializer(serializers.ModelSerializer):
#     is_sub = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Course
#         fields = ('name', 'is_sub')
#
#
# class CourseDetailSerializer(serializers.ModelSerializer):
#     count_lessons = serializers.SerializerMethodField()
#     lesson = serializers.SerializerMethodField()
#
#     def get_lessons_count(self, obj):
#         return obj.lessons_set.all().count()
#
#     def get_lessons(self, obj):
#         return [i.pk for i in obj.lessons.all()]
#
#     class Meta:
#         model = Course
#         fields = ('name', 'about', 'count_lessons')
#
#
# class CourseCreateSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         course = Course(
#             name=validated_data['name'],
#             about=validated_data['about'],
#         )
#         course.save()
#         return course
#
#     class Meta:
#         model = Course
#         fields = ('name', 'about')
