from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    ListAPIView, GenericAPIView
)
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .auth_token import BearerTokenAuthentication
from .models import ProductApi
from .paginations import BaseSetPagination
from .serializers import ProductApiSerializer
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication

# @api_view(['GET'])
# def get_products(request):
#     products = ProductApi.objects.all()[:10]
#     output = []
#     for product in products:
#         output.append({'name': product.name, 'price': product.price,'amount':product.amount})
#     return JsonResponse(output, safe=False)
# import pdb;pdb.set_trace()
# return Response({"message": "Hello, world!"})

# class ProductsList(APIView):
#     def get(self, request, format=None):
#         products = [{"id":product.id,'name': product.name, 'price': product.price,'amount':product.amount} for product in ProductApi.objects.all()]
#         return Response(products)
#     def post(self, request, format=None):
#         serializer = ProductApiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ProductDetail(APIView):
#     def get_object(self, id):
#         try:
#             return ProductApi.objects.get(id=id)
#         except Exception:
#             raise Http404
#
#     def get(self, request, id, format=None):
#         product = self.get_object(id)
#         serializer = ProductApiSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, id, format=None):
#         product = self.get_object(id)
#         serializer = ProductApiSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def patch(self, request, id):
#         product = self.get_object(id)
#         serializer = ProductApiSerializer(product, data=request.data, partial=True) # set partial=True to update a data partially
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id, format=None):
#         product = self.get_object(id)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class ReadOnly:
    pass


class ProductsList(ListAPIView):
    # authentication_classes = [BearerTokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name', 'amount']
    ordering_fields = ['name', 'amount']
    search_fields = ['name', 'price']
    ordering = ['-price']
    pagination_class = BaseSetPagination


class ProductDetail(RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericAPIView):
    # authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = ProductApi.objects.all()
    serializer_class = ProductApiSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class ProductsList(ListCreateAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
#
# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ProductApi.objects.all()
#     serializer_class = ProductApiSerializer
