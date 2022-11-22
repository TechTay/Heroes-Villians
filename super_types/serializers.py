from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.modelSerializer):
    class Meta:
        type = SuperType
        fields = ['Super_Type']