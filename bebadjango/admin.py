from django.contrib import admin

from .models import *

admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Payment)
admin.site.register(Booking)