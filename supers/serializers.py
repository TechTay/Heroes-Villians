from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.modelSerializer):
    class Meta:
        type = Supers
        fields = ['name','alter_ego','primary_ability','secondary_ability','catchphrase','super_type']