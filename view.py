from rest_framework import generics
from .models import YapayZekaModel
from .serializers import YapayZekaModelSerializer

class YapayZekaModelListCreateView(generics.ListCreateAPIView):
    queryset = YapayZekaModel.objects.all()
    serializer_class = YapayZekaModelSerializer