from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import Car
from ..serializers.get_car_serializers import DisplayCarSerializer
from parkingfee.utils.constants import *

import pytz
from django.http import Http404





class EditCarDetailsViews(APIView):

    def get_car(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
    def put(self,request,pk):
        data = {}
        errors = {}
        status = None
        message = None
        car = self.get_car(pk)
        plate_number = request.data.get('plate_number', car.plate_number)
        if Car.objects.filter(plate_number=plate_number).exclude(pk=pk).exists():
            message = 'This plate number is already taken'
            status = bad_request
            data = {'plate_number': plate_number}
            return Response({"Message": message, "data": data, "status": status, "errors": errors})
        serializer= DisplayCarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            message = 'Successfully Updated'
            status = ok
        else:
            data = serializer.data
            message = 'Error'
            status = bad_request

        return Response({"message": message, "data": data, "status": status, "errors": serializer.errors})
    
