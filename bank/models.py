from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Here models means the table the data are stored into
# We donot write raw sql here Instead of that django provides an ORM(Object Relation Mapper) which is written on python 
# We write Class and objects in python here and ORM comverts them into the database tables 



# the token table is created here which have tuples like customer,bank,created and status
class Bank_Token(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    token_number=models.CharField(max_length=10,unique=True)
    bank_name=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-id'] #Order by descending id

