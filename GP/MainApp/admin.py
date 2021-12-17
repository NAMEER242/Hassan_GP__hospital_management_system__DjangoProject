from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Reservation)
admin.site.register(Employee)
