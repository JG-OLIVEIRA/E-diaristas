from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DiaristasCidadesPagination(PageNumberPagination):
    page_size = 6

    def get_paginated_response(self, data):
        return Response({
            'quatidade_diaristas': (self.page.paginator.count - self.page_size)
             if self.page.paginator.count > self.page_size else 0,
            'diaristas': data
        })