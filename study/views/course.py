# для курса через ViewSets
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from study.paginators import CoursePaginator
from study.permissions import IsModerator, IsOwner
from study.seriallizers.course import Course, CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def get_permissions(self):
        # Проверка разрешения для разных методов
        if self.action == 'create':
            permissions_classes = [IsAuthenticated]
        elif self.action == 'update':
            permissions_classes = [IsModerator | IsOwner]
        else:
            permissions_classes = [AllowAny]

        return [permission() for permission in permissions_classes]

    # def list(self, request, **kwargs):
    #     queryset = Course.objects.all()
    #     serializer = CourseListSerializer(queryset, many=True)
    #
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None, **kwargs):
    #     queryset = Course.objects.all()
    #     course = get_object_or_404(queryset, pk=pk)
    #     serializer = CourseDetailSerializer(course)
    #
    #     return Response(serializer.data)
    #
    # # def create(self, request, *args, **kwargs):
    # #     queryset = Course.objects.all()
    # #     serializer = CourseCreateSerializer(queryset, many=True)
    # #
    # #     return Response(serializer.data)



