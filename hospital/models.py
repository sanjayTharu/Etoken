from django.db import models
from django.contrib.auth.models import User
# from bank.models import Customer
# Create your models here.

class Hospital_Token(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    token_number=models.CharField(max_length=10,unique=True)
    hospital_name=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-id'] #Order by descending id
        ordering=['-id']

    @property
    def token_number(self):
        return f"T{self.id:04d}"
    def __str__(self):
        return f"Token: {self.token_number}"
    