from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Office_Token)
class OfficeTokenAdmin(admin.ModelAdmin):
    list_display=['id','customer','token_number','office_name','created_at']