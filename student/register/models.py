from django.db import models

class details(models.Model):
    studentfname=models.CharField(max_length=100)
    studentlname=models.CharField(max_length=100)
    studentnumber=models.IntegerField()
    studentemail=models.CharField(max_length=100)
    studentcourse=models.CharField(max_length=100)
    studentaddress=models.CharField(max_length=100)
