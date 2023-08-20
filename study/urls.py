from django.urls import path
from rest_framework import routers

from study.apps import StudyConfig
from study.views.lesson import LessonListView, LessonDetailView, LessonDeleteView, LessonUpdateView, LessonCreateView
from study.views.course import *

app_name = StudyConfig.name

urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_item'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
