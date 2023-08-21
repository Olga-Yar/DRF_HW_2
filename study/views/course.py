# для курса через ViewSets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from study.permissions import IsModerator, IsOwner
from study.seriallizers.course import CourseDetailSerializer, Course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]
