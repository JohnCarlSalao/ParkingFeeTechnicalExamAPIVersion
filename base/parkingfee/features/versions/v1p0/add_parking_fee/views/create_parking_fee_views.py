from rest_framework.views import APIView
from parkingfee.models import Car, ParkingFee
from parkingfee.utils.generate_uid import generate_uuid
from parkingfee.utils.constants import *
from ..serializers.create_parking_fee_serializers import CreateParkingFeeSerializer
from rest_framework.response import Response
import datetime

class CreateParkingFeeViews(APIView):
    def post(self, request):
        uid = generate_uuid()
        serializer = CreateParkingFeeSerializer(data=request.data)

        if serializer.is_valid():
            car_id = request.data['car']
            try:
                car = Car.objects.get(id=car_id)
            except Car.DoesNotExist:
                return Response({
                    "status": not_Found,
                    "message": f"Car with id {car_id} does not exist",
                    "data": {},
                    "errors": {}
                })

            entry_time_str = request.data['entry_time']

            entry_time = datetime.datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
            exit_time = datetime.datetime.now()

            time_diff = exit_time - entry_time
            total_hours = int(time_diff.total_seconds() / 3600)
            total_amount = 50 + max(0, total_hours - 3) * 10

            vat = total_amount * 0.12
            vat_sales = total_amount - vat

            entry_time_formatted = entry_time.strftime('%I:%M %p')
            exit_time_formatted = exit_time.strftime('%I:%M %p')

            parking_fee = ParkingFee.objects.create(
                id=uid,
                car=car,
                entry_time=entry_time,
                exit_time=exit_time,
                total_amount=total_amount
            )

            serializer = CreateParkingFeeSerializer(parking_fee)
            data = serializer.data
            data['total_amount'] = total_amount
            data['vat'] = vat
            data['vat_sales'] = vat_sales
            data['entry_time_formatted'] = entry_time_formatted
            data['exit_time_formatted'] = exit_time_formatted
            data['parking_hours'] = total_hours
            status = "created"
            errors = {}
            message = 'Successfully created ParkingFee'
        else:
            data = {}
            status = "error"
            errors = serializer.errors
            message = 'Invalid data'

        return Response({
            "status": status,
            "message": message,
            "data": data,
            "errors": errors
        })