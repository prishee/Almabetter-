from django.db import models

# Create your models here.
class Mark(models.Model):
  rollNo=models.CharField(max_length=10)
  name=models.CharField(max_length=20)
  marksInMaths=models.IntegerField()
  marksInPhysics=models.IntegerField()
  marksInChemistry=models.IntegerField()

