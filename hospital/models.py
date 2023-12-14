from django.db import models
from typing import Any,Dict, Tuple
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    class Meta:
        app_label = 'hospital'

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        app_label = 'hospital'

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    # Agrega más campos según sea necesario
#me olvide cambiarlos pero Usuario vendria a representar Citas, perdon :C
class Usuario(models.Model):
    
    nombre_paciente       =  models.AutoField( primary_key=True, db_column='id')
    nombre_doc  =  models.CharField(max_length=30, blank=False, null=False)
    fechayhora     =  models.CharField(max_length=50, blank=False, null=False)


    def __str__(self):
        return str(self.nombre_paciente)