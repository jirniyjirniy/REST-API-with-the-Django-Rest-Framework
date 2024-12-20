from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductListApiView(generics.ListAPIView):
    """
    Not to use
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListApiView.as_view()


@api_view(['POST', 'GET'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        qs = Product.objects.all()  # qs = queryset
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if method == 'POST':
        # create an item
        # create view
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            return Response(serializer.data)
        return Response({'invalid': 'not good data'})
