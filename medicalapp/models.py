from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

DISEASE_CHOICES = [
    ('Diabetes', 'Diabetes'),
    ('BP', 'Blood Pressure'),
    ('Heart', 'Heart Disease'),
    ('Asthma', 'Asthma'),
]
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=[('Male', 'Male'),('Female', 'Female')])
    document_proof = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(['pdf'])])
    previous_report = models.FileField(
        upload_to='reports/',
        validators=[FileExtensionValidator(['pdf'])],
        null=True,
        blank=True)
    existing_diseases = models.CharField(max_length=100,blank=True,null=True,default="" )
    created_at = models.DateTimeField(auto_now_add=True)
    problem = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=15,null=True,blank=True)
    agreement = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"