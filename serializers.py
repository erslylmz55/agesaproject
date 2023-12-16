from rest_framework import serializers
from .models import YapayZekaModel

class YapayZekaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YapayZekaModel
        fields = '__all___'