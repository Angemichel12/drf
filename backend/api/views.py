from rest_framework.response import Response
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        
        print(serializer.data)
        return Response(serializer.data, status=200)
    return Response({"message":"Invalid data"})
    

