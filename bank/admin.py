from django.contrib import admin
from .models import *
# Register your models here.B

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','phone','email','address']

@admin.register(Bank_Token)
class TokenAdmin(admin.ModelAdmin):
    list_display=['id','customer','created_at','status']