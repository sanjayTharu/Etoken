from django.db import models

# Create your models here.
# Here models means the table the data are stored into
# We donot write raw sql here Instead of that django provides an ORM(Object Relation Mapper) which is written on python 
# We write Class and objects in python here and ORM comverts them into the database tables 

# the Customer table is created here which has tuples like name,phone,email,address and it returns the name attribute
# the id field is auto genereted by the orm thw qurey can be seen on the migrations folder the changes and the qurey creation are stored there.
class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=250)
    address=models.CharField(max_length=250)


    def __str__(self):
        return self.name
    
# the token table is created here which have tuples like customer,bank,created and status
class Bank_Token(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # bank=models.CharField(max_length=150,choices=(
    #     ('RASTRIYA BANIJYA BANK LIMITED','Rastriya Banijya Bank Limited'),
    #     ('NEPAL BANK LIMITED','Nepal Bank Limited'),
    #     ('SIDDHARTHA BANK LIMITED ','Siddhartha Bank Limited'),
    #     ('AGRICULTURE DEVELOPMENT BANK LIMITED', 'Agriculture Development Bank Limited')
    # ),default='RASTRIYA BANIJYA BANK LIMITED')
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,choices=(
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('COMPLETED','Completed'),
        ('CANCELED','Canceled')
    ),default='PENDING')

    class Meta:
        ordering=['-id'] #Order by descending id

    @property
    def token_number(self):
        #calculate token number based on object id
        return f"T(self.id:04d)"
    
    def __str__(self):
        return f"Token:{self.token_number}-{self.customer.name}"
