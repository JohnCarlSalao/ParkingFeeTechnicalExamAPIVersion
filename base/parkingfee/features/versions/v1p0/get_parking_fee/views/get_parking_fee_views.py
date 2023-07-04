from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import ParkingFee
from ..serializers.get_parking_fee_serializers import DisplayParkingFeeSerializer
import pytz
from parkingfee.utils.constants import*
from django.http import Http404






class DisplayParkingFeeViews(APIView):    
    def get(self, request):
        parking_fees = ParkingFee.objects.all().select_related('car')
        
        data = []
        for fee in parking_fees:
            fee_data = {
                'id': fee.id,
                'car_brand': fee.car.car_brand,
                'car_model': fee.car.car_model,
                'plate_number': fee.car.plate_number,
                'entry_time': fee.entry_time,
                'exit_time': fee.exit_time
            }
            
            
            total_hours = int((fee.exit_time - fee.entry_time).total_seconds() / 3600)
            parking_fee = 50 + max(0, total_hours - 3) * 10
            vat = parking_fee * 0.12
            vat_sales = parking_fee - vat
            
            fee_data['parking_fee'] = parking_fee
            fee_data['vat'] = vat
            fee_data['vat_sales'] = vat_sales
            
            data.append(fee_data)
        
        message = 'Success'
        status = 'ok'
        return Response({"message": message, "data": data, "status": status})
        







