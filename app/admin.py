from django.contrib import admin

from .models import Patient,Investigation,Doctors,MedicalSpecialty,Consultation

admin.site.register(Patient)
admin.site.register(Investigation)
admin.site.register(MedicalSpecialty)
admin.site.register(Consultation)

# Register your models here.
