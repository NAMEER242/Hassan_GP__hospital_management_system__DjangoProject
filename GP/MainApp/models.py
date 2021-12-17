from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid


class CustomUser(AbstractUser):
    ID = models.IntegerField(primary_key=True)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    certification_image = models.ImageField(upload_to="images", blank=True)
    specialization = models.TextField()
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images")
    ID = models.IntegerField(primary_key=True)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    patientAddress = models.CharField(max_length=1000)
    age = models.IntegerField()
    notes = models.TextField()
    ID = models.IntegerField(primary_key=True)


class Reservation(models.Model):
    P_name = models.CharField(max_length=100)
    P_age = models.IntegerField()
    gender = models.CharField(max_length=10)
    reservations_date = models.IntegerField()
    PID = models.IntegerField()
    DID = models.IntegerField()
    ID = models.IntegerField(primary_key=True)

    class Meta:
        ordering = ("-reservations_date",)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    salary = models.CharField(max_length=50)
    ID = models.IntegerField(primary_key=True)
