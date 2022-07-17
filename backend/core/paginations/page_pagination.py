import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    max_page_size = 100
    page_size_query_param = 'size'
    page_size = 100

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_page = math.ceil(count / self.get_page_size(self.request))
        return Response({
            'total_items': count,
            'total_page': total_page,
            'prev': self.get_previous_link(),
            'next': self.get_next_link(),
            'data': data
        })
