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
import datetime
import calendar
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from collections import OrderedDict

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


from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@permission_classes((permissions.AllowAny,))
class totals(APIView):
    def get(self, request, format=None):
        """
        Return totals
        """
        drivers= str(Driver.objects.count())
        bookings= str(Booking.objects.count())
        passengers= str(Passenger.objects.count())
        payments= str(Payment.objects.count())
        data = {'drivers':drivers,'bookings':bookings,'passengers':passengers,'payments':payments}
        return Response(OrderedDict(sorted(data.items()))) #order 


@permission_classes((permissions.AllowAny,))
class historical_data(APIView):
    def get(self, request, format=None):
        data = {} #for storing data
        #last five months 
        lfm = list(range((datetime.datetime.now().month-4),datetime.datetime.now().month+1))
        months = [calendar.month_name[x] for x in lfm]
        data['months'] = months


        d =list(Driver.objects.annotate(month=ExtractMonth('date_joined')).values('month').annotate(c=Count('id')).values('month', 'c'))
        b =list(Booking.objects.annotate(month=ExtractMonth('date')).values('month').annotate(c=Count('id')).values('month', 'c'))
        pt =list(Payment.objects.annotate(month=ExtractMonth('date')).values('month').annotate(c=Count('id')).values('month', 'c'))
        pr =list(Passenger.objects.annotate(month=ExtractMonth('date_joined')).values('month').annotate(c=Count('id')).values('month', 'c'))

        #Function creates dict values where k=month and v=no_of_hits. I use OrderedDict to
        #order by month. I also put zeros for months with no hits
        def gen(kk,name):
            monthlydata = {}
            for k in kk:
                try:
                    monthlydata[k['month']]=monthlydata[k['month']]+1
                except KeyError:
                    monthlydata[k['month']]=1
            #put zeros for months with no hits
            for m in lfm:
                if m not in monthlydata.keys():
                    monthlydata[m]=0
            ordered_monthlydata = OrderedDict(sorted(monthlydata.items()))

            return {'name':name, 'data':ordered_monthlydata.values()}

        #Apply the function defined above to all relevant 'items' to output a list of key value pairs
        mylist = [gen(x[0],x[1]) for x in [(d,'driver'),(b,'bookings'),(pt,'payments'),(pr,'passengers')] ]
        mylist_ = sorted(mylist, key=lambda k: k['name']) #sort by name (driver,bookings...etc)


        data['monthly_counts'] = mylist_
        return Response(data)




