from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display=['id','name','age','gender','phone_number','email','address']

@admin.register(Office_Token)
class OfficeTokenAdmin(admin.ModelAdmin):
    list_display=['id','citizen','created_at','status']