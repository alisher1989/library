from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets, pagination
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer


class BookPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class BookViewSet(viewsets.ModelViewSet):
    """Список книг"""
    pagination_class = BookPagination

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @method_decorator(cache_page(60*2))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



