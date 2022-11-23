from rest_framework import serializers
from .models import Supers


class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name','alter_ego','primary_ability','secondary_ability','catchphrase','super_type',]
        depth = 1
        super_type = serializers.IntegerField(write_only=True)