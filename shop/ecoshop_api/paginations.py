from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BaseSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('items', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page_size', self.page_size),
            ('data', data)
        ]))