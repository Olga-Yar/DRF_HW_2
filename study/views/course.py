# для курса через ViewSets
from rest_framework.viewsets import ModelViewSet

from study.seriallizers.course import CourseDetailSerializer, Course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
