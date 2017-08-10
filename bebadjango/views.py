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


@login_required(login_url='accounts/login/')
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
        return render_to_response('index.html')
        
    else:
        # Return an 'invalid login' error message.
        context = {'msg': "Please enter the correct username and password!!!"}
        return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render_to_response('registration/login.html',{'msg':'logged out'})
    #context = {'msg': "Successfully logged out!!!"}
    #return render( 'registration/login.html')

# @login_required(login_url='/accounts/login/')
def create_user(request,username, email, password):
	user = User.objects.create_user(username, email, password)
    #u.save()
    # Redirect to a success page.
    #return render_to_response('index.html',{'msg':'User Successfully Created'})


@login_required(login_url='/accounts/login/')
def change_password(request,username,new_password):
	u = User.objects.get(username=username)
	u.set_password(new_password)
	#u.save()
	# Redirect to a success page.
    #return render_to_response('index.html',{'msg':'Password Successfully Reset'})


@login_required(login_url='/accounts/login/')
def passengers(ListView):
    model = Passenger

@login_required(login_url='/accounts/login/')
def bookings(ListView):
    model = Booking

@login_required(login_url='/accounts/login/')
def payments(ListView):
    model = Payment


#views
class DriverView(ListView):
        context_object_name = 'driverview'
        queryset = Driver.objects.all()
        template_name = 'drivers.html'

class PaymentView(ListView):
        context_object_name = 'paymentview'
        queryset = Payment.objects.all()
        template_name = 'payments.html'

class PassengerView(ListView):
        context_object_name = 'passengerview'
        queryset = Passenger.objects.all()
        template_name = 'passengers.html'


class BookingView(ListView):
        context_object_name = 'bookingview'
        queryset = Booking.objects.all()
        template_name = 'bookings.html'


def DashboardView(request):
    return render(request, 'dashboard.html')


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

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_totals(self,request):
        return Response(Booking.objects.count())

class totals(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return self.Response(usernames)