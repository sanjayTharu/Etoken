from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','name','age','gender','phone_number','email','address']

@admin.register(Hospital_Token)
class HospitalTokenAdmin(admin.ModelAdmin):
    list_display=['id','patient','created_at','status']