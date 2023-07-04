from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import ParkingFee
from parkingfee.utils.constants import*

from django.http import Http404




class GetParkingFeeDetailsViews(APIView):
    def get_car_parking_fee(self, pk):
        try:
            return ParkingFee.objects.get(pk=pk)
        except ParkingFee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        

        parking_fee = self.get_car_parking_fee(pk)

        total_hours = int((parking_fee.exit_time - parking_fee.entry_time).total_seconds() / 3600)
        parking_fee_amount = 50 + max(0, total_hours - 3) * 10
        vat = parking_fee_amount * 0.12
        vat_sales = parking_fee_amount - vat

        data = {
            'id': parking_fee.id,
            'car_brand': parking_fee.car.car_brand,
            'car_model': parking_fee.car.car_model,
            'plate_number': parking_fee.car.plate_number,
            'entry_time': parking_fee.entry_time,
            'exit_time': parking_fee.exit_time,
            'parking_fee': parking_fee_amount,
            'vat': vat,
            'vat_sales': vat_sales,
            'total_hours': total_hours
        }

        status = ok
        message = 'Results'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})