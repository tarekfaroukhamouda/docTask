from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
class Patient(models.Model):
    Name=models.CharField(max_length=200,default='')
    patient=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
         return self.Name
class Doctors(models.Model):
    doctor=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        self.doctor.username
class Investigation(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    InvestigationTitle=models.CharField(max_length=200)
    InvestigationFile=models.FileField()
    InvestigationDate=models.DateTimeField()
    def __str__(self):
        return self.InvestigationTitle+" "+str(self.InvestigationFile)

class MedicalSpecialty(models.Model):
    Specialty=models.CharField(max_length=50)
    def __str__(self):
        return self.Specialty
class Consultation(models.Model):
    MedicalSpecialty=models.ForeignKey(MedicalSpecialty,on_delete=models.CASCADE)
    Investigations=models.ManyToManyField(Investigation)
    MedicalComplaint=models.TextField()
    ConsultationDate=models.DateTimeField()


    



        

# Create your models here.
