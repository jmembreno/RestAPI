from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Breed(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=6,choices=(('T',"Tiny",),('S',"Small",),('M',"Medium",),('L',"Large",),) )
    Friendliness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Trainability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Sheddingamount = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Exerciseneed = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE,related_name="dogs")
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=50)
    favoritetoy = models.CharField(max_length=50)
