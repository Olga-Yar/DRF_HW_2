# для урока через дженерики
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from study.seriallizers.lesson import LessonBaseSerializer, Lesson


class LessonBaseAPIView:
    queryset = Lesson.objects.all()
    serializer_class = LessonBaseSerializer


class LessonDetailView(LessonBaseAPIView, RetrieveAPIView):
    pass


class LessonDeleteView(LessonBaseAPIView, DestroyAPIView):
    pass


class LessonListView(LessonBaseAPIView, ListAPIView):
    pass


class LessonUpdateView(LessonBaseAPIView, UpdateAPIView):
    pass


class LessonCreateView(LessonBaseAPIView, CreateAPIView):
    pass
