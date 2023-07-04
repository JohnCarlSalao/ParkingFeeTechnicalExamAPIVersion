"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from parkingfee.features.versions.v1p0.add_parking_fee.views.create_parking_fee_views import CreateParkingFeeViews
from parkingfee.features.versions.v1p0.create_car.views.create_car_views import CreateCarViews
from parkingfee.features.versions.v1p0.display_car.views.display_car_views import DisplayCarViews
from parkingfee.features.versions.v1p0.get_car_details.views.get_car_details_views import GetCarDetailsViews
from parkingfee.features.versions.v1p0.delete_car.views.delete_car_details_views import DeleteCarDetailsViews
from parkingfee.features.versions.v1p0.edit_car_details.views.edit_car_details_views import EditCarDetailsViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('parking/add/create-parking-fee/', CreateParkingFeeViews.as_view(), name='create-parking-fee'),
    path('car/create/', CreateCarViews.as_view(),name='create-car'),
    path('car/get/all/', DisplayCarViews.as_view(),name='display-all-car'),
    path('car/details/<pk>/', GetCarDetailsViews.as_view(), name = 'get-car-details'),
    path('car/details/delete/<pk>/', DeleteCarDetailsViews.as_view(), name ='delete-car-details'),
    path('car/details/edit/<pk>/', EditCarDetailsViews.as_view(), name ='edit-car-details'),

]
