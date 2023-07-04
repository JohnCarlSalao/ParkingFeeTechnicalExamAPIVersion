from rest_framework.views import APIView
from parkingfee.models import Car
from parkingfee.utils.generate_uid import generate_uuid
from parkingfee.utils.constants import *
from ..serializers.display_car_serializers import DisplayCarSerializer
from rest_framework.response import Response
import pytz

class DisplayCar(APIView):    
    def get(self, request):
        
        car = Car.objects.all().values('id', 'car_brand', 'car_model', 'plate_number')
        data = car
        message = 'Success'
        status = ok 
        return Response({"Message": message, "data": data, "status": status})