from rest_framework import serializers
from parkingfee.models import Car

class DisplayCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_brand', 'car_model', 'plate_number']

