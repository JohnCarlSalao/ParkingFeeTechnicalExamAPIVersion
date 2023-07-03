from rest_framework.views import APIView
from parkingfee.models import Car, ParkingFee
from parkingfee.utils.generate_uid import generate_uuid
from parkingfee.utils.constants import *
from ..serializers.create_parking_fee_serializers import CreateParkingFeeSerializer
from rest_framework.response import Response

class CreateParkingFee(APIView):
    def post(self, request):
        uid = generate_uuid()
        serializer = CreateParkingFeeSerializer(data=request.data)
        
        if serializer.is_valid():
            parking_fee = ParkingFee.objects.create(
                id=uid,
                car=request.data['car'],
                entry_time=request.data['entry_time']
            )
            serializer = CreateParkingFeeSerializer(parking_fee)
            data = serializer.data
            status = created
            errors = {}
            message = 'Successfully created ParkingFee'
        else:
            data = {}
            status = bad_request
            errors = serializer.errors
            message = 'Invalid data'

        return Response({
            "status": status,
            "message": message,
            "data": data,
            "errors": errors
        })