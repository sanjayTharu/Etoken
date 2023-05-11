from django.contrib import admin
from .models import *
# Register your models here.B


@admin.register(Bank_Token)
class TokenAdmin(admin.ModelAdmin):
    list_display=['id','customer','token_number','bank_name','created_at']