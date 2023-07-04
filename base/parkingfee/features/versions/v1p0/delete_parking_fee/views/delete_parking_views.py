from rest_framework.views import APIView
from rest_framework.response import Response 
from parkingfee.models import ParkingFee


from django.http import Http404
from parkingfee.utils.constants import *





class DeleteParkingFeeViews(APIView):
    def get_parking_fee(self, pk):
        try: 
            return ParkingFee.objects.filter(pk=pk).get()
        except ParkingFee.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        errors = {}
        data = {}
        status = None
        car = self.get_parking_fee(pk)
        car.delete()
        message = 'Successfully Deleted'
        status = no_content        
        return Response ({"message": message, "data": data, "status": status, "errors": errors })
    