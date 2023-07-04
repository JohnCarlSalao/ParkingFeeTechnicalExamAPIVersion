from rest_framework.views import APIView
from rest_framework.response import Response
from parkingfee.models import Car
from parkingfee.utils.constants import *
from parkingfee.utils.generate_uid import generate_uuid
from ..serializers.create_car_serializers import CreateCarSerializer



class CreateCar(APIView):    
    def post(self, request):
        serializer = CreateCarSerializer(data=request.data)
        data = {}
        errors = {}
        status = None
        message = None
       

        if serializer.is_valid():
            
            uid = generate_uuid()
            car = Car.objects.create(id = uid,
                                     car_brand = request.data['car_brand'],
                                     car_model = request.data['car_model'], 
                                     plate_number=request.data['plate_number'])
            car=  Car.objects.filter(id=uid).values('id','car_brand','car_model','plate_number')
            data=car
            errors = serializer.errors
            status = created
            message = 'Successfully Created'
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        errors = serializer.errors
        status = bad_request
        return Response({"message": "error!", "status": status, "errors": serializer.errors})
