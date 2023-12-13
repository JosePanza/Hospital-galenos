from django.db import models

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

class Usuario(models.Model):
    ID_usuario       =  models.AutoField( primary_key=True, db_column='id')
    nombre_usuario   =  models.CharField(max_length=30, blank=False, null=False)
    descripcion      =  models.CharField(max_length=50, blank=False, null=False)
    img              =  models.FileField(upload_to='img/', null=False, blank=False, verbose_name='img')


    def __str__(self):
        return str(self.ID_usuario)