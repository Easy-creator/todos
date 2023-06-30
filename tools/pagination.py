from rest_framework import pagination

class CustomPagePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 1000
    page_query_param = 'p'