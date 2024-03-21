from django.db import models



class regtable(models.Model):
    name=models.CharField(max_length=150)
    age=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=150)
    
