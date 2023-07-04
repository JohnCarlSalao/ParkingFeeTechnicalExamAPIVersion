from rest_framework import serializers
from parkingfee.models import ParkingFee

class CreateParkingFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingFee
        fields = ['car', 'entry_time', 'exit_time', 'total_amount']


