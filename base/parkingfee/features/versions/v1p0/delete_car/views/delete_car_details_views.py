from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import Car
from ..serializers.delete_car_serializers import DisplayCarSerializer
import pytz
from django.http import Http404
from parkingfee.utils.constants import *





class DeleteCarDetailsViews(APIView):
    def get_car(self, pk):
        try: 
            return Car.objects.filter(pk=pk).get()
        except Car.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        errors = {}
        data = {}
        status = None
        car = self.get_car(pk)
        car.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"Message": message, "data": data, "status": status, "errors": errors })
    