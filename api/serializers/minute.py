from rest_framework import serializers
from minute.models import Minute

class MinuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minute
        fields = ('club','action_by','minute','agenda','attendes')
        read_only_fields = ('action_by',)