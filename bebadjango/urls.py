"""bebadjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from . import views
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^accounts/login/$', views.login),
    # url(r'^logout/$', views.logout),
    # url(r'^changepassword/$', views.change_password),
    url(r'^create_user/(?P<username>[0-9A-Za-z]+)/(?P<password>[0-9A-Za-z]+)/(?P<email>[0-9A-Za-z_@.]+)/$', views.create_user),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #User Dashboard 
    url(r'^drivers/$', views.DriverView.as_view()),
    url(r'^passengers/$', views.PassengerView.as_view()),
    url(r'^payments/$', views.PaymentView.as_view()),
    url(r'^bookings/$', views.BookingView.as_view()),
    url(r'^reports/$', views.DashboardView),


    #API
    url(r'^api/bookings/$', views.BookingList.as_view()),
    url(r'^api/bookings/(?P<pk>[0-9]+)/$', views.BookingDetail.as_view()),
    url(r'^api/drivers/$', views.DriverList.as_view()),
    url(r'^api/drivers(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
    url(r'^api/passengers/$', views.PassengerList.as_view()),
    url(r'^api/passengers/(?P<pk>[0-9]+)/$', views.PassengerDetail.as_view()),
    url(r'^api/payments/$', views.PaymentList.as_view()),
    url(r'^api/payments/(?P<pk>[0-9]+)/$', views.PaymentDetail.as_view()),
    url(r'home$', views.index,name='index'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
