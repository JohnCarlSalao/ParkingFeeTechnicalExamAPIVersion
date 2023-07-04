from rest_framework import serializers
from parkingfee.models import ParkingFee

class DisplayParkingFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingFee
        fields = ['id','car', 'entry_time', 'exit_time', 'total_amount']


