from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import Car
from ..serializers.get_car_serializers import DisplayCarSerializer
import pytz
from django.http import Http404





class GetCarDetailsViews(APIView):

    def get_car(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        phil_tz = pytz.timezone('Asia/Manila')

        car = self.get_car(pk)
        serializer = DisplayCarSerializer(car)
        
        data = serializer.data
        

        status = 'ok'
        message = 'Results'
        errors = {}

        return Response({"message": message, "data": data, "status": status, "errors": errors})