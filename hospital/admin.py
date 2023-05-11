from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Hospital_Token)
class HospitalTokenAdmin(admin.ModelAdmin):
    list_display=['id','customer','token_number','hospital_name','created_at']