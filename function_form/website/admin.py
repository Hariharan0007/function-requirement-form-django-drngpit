from django.contrib import admin

from .models import admin_model,staff_model,function_model,venue_model,booking_model


# Register your models here.

admin.site.register(admin_model)
admin.site.register(staff_model)
admin.site.register(function_model)
admin.site.register(venue_model)
admin.site.register(booking_model)