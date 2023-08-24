# для урока через дженерики
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from study.paginators import LessonPaginator
from study.permissions import IsModerator, IsOwner

from study.seriallizers.lesson import LessonBaseSerializer, Lesson


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonBaseSerializer


class LessonDetailView(LessonBaseAPIView, RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]


class LessonDeleteView(LessonBaseAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]


class LessonListView(LessonBaseAPIView, ListAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonUpdateView(LessonBaseAPIView, UpdateAPIView):
    permission_classes = [IsAuthenticated, IsModerator|IsOwner]


class LessonCreateView(LessonBaseAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
