from rest_framework import generics, permissions, authentication,mixins
from .models import Product
from .serializers import ProductSerializer
from api.mixins import IsStaffEditorPermissionMixin
from api.authentications import TokenAuthentication

class ProductListCreateAPIView(IsStaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if not content:
            content = title
            print(content)
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()
class ProductDetailAPIView(IsStaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(IsStaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_apiveiw = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(IsStaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
product_destroy_apiview = ProductDestroyAPIView.as_view()

"""
This is my own Product view using mixins with:
- Get all products and product detail.
- Post products
- Update Products
- Delete Products
"""

# class ProductViewMaxims(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def get(self,request,*args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
        
#         return self.list(request, *args, **kwargs)
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#     def perform_create(self,serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if not content:
#             content = title
#         serializer.save(content=content)

#     def patch(self,request,*args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
        



















# class ProductMixinView(mixins.ListModelMixin,
#                        mixins.RetrieveModelMixin,
#                        mixins.CreateModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.DestroyModelMixin, 
#                        generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def get(self,request, *args,**kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         if not content:
#             content = "This is cool stuff by mixin"
#             print(content)
#         serializer.save(content=content)
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# product_mixin_view = ProductMixinView.as_view()