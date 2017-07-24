from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,render_to_response,get_object_or_404
from bebadjango.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from bebadjango.models import *
from django.views.generic.edit  import CreateView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from bebadjango.serializer import BookingSerializer,DriverSerializer,PaymentSerializer,PassengerSerializer


@login_required(login_url='/accounts/login/')
def index(request):
	# return render_to_response('index.html', {'data': "Yahweh is a great God!!!"})
	context = {'data': "Yahweh is a great God!!!"}
	return render(request, 'index.html', context)


def login(request):
	return render_to_response('registration/login.html')

@login_required(login_url='/accounts/login/')
def auth(request):
    usernm = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=usernm, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        pass

@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    # Redirect to a success page.

# @login_required(login_url='/accounts/login/')
def create_user(request,username, email, password):
	user = User.objects.create_user(username, email, password)
	# Redirect to a success page.

@login_required(login_url='/accounts/login/')
def change_password(request,username,new_password):
	u = User.objects.get(username=username)
	u.set_password(new_password)
	u.save()
	# Redirect to a success page.


@login_required(login_url='/accounts/login/')
def passengers(ListView):
    model = Passenger

@login_required(login_url='/accounts/login/')
def bookings(ListView):
    model = Booking

@login_required(login_url='/accounts/login/')
def payments(ListView):
    model = Payment



class myDriver(ListView):
     # template_name = 'drivers.html'
     # context_object_name = 'my_drivers'

     # def get_queryset(self):
     #     self.driver = get_object_or_404(Driver, name=self.args[0])
     #     return Driver.objects.filter(driver=self.driver)

     # model = Driver

        context_object_name = 'my_drivers'
        queryset = Driver.objects.all()
        template_name = 'drivers.html'


#API
class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


        
class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class PassengerList(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
        
class PassengerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
        
class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
        
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer