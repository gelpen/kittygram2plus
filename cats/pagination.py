# cats/pagination.py
from rest_framework.pagination import PageNumberPagination


class CatsPagination(PageNumberPagination):
    page_size = 2