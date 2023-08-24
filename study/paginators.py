from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 2
    page_query_param = 'page-size'
    max_page_size = 50


class LessonPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = 'page-size'
    max_page_size = 50
