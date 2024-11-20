import json

from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Product
from products.serializers import ProductSerializer

#
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     #     print(data)
#     #     data = dict(data)
#     #     json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
#     return JsonResponse(data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        # data = serializer.data
        return Response(serializer.data)
