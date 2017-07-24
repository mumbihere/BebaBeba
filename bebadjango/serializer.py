from rest_framework import serializers
from bebadjango.models import Driver,Booking,Payment,Passenger
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = ('id','name','email')

class PassengerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = ('id','name','email')

class BookingSerializer(serializers.ModelSerializer):
	driver = DriverSerializer()
	passenger = PassengerSerializer()
	class Meta:
		model = Booking
		fields = ('driver','passenger','date')


class PaymentSerializer(serializers.ModelSerializer):
	passenger = PassengerSerializer()
	class Meta:
		model = Payment
		fields = ('passenger','date','amount')