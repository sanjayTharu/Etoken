from django.db import models

# Create your models here.
class Citizen(models.Model):
    name= models.CharField(max_length=200)
    age=models.IntegerField()
    gender= models.CharField(max_length=150,choices=(
        ('MALE','Male'),
        ('FEMALE','Female'),
        ('OTHER','Other'),
    ),default='MALE')
    phone_number=models.BigIntegerField()
    email=models.EmailField(max_length=150)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Office_Token(models.Model):
    citizen=models.ForeignKey(Citizen,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=150,choices=(
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('COMPLETED','Completed'),
        ('CANCELLED','Cancelled'),
    ),default='PENDING')

    class Meta:
        ordering=['-id']
    @property
    def token_number(self):
        return f"T{self.id:04d}"
    
    def __str__(self):
        return f"Tokeen: {self.token_number}-{self.citizen.name}"