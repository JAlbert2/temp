from django.db import models

# Create your models here.


class Patient(models.Model):
    user = models.CharField(max_length=200)
    creation = models.DateTimeField('creation')
    age = models.IntegerField()
    covid = models.BooleanField()
    UID = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.UID)

class xapi(models.Model):
    uuid = models.CharField(max_length=40)
    interactionType = models.CharField(max_length=15)
    objectLink = models.CharField(max_length=200) 
    localId = models.IntegerField()
    objectName = models.CharField(max_length=100)
    correct = models.CharField(max_length=500)
    answers = models.CharField(max_length=1500)
    description = models.CharField(max_length=500)
    categoryId = models.CharField(max_length=500)
    minScore = models.IntegerField()
    maxScore = models.IntegerField()
    raw = models.FloatField()
    scaled  = models.FloatField()
    completion = models.BooleanField()
    success = models.BooleanField()
    response = models.IntegerField()
    
    def __str__(self):
        return str(self.uuid)
        
class xapiRaw(models.Model):
    UID = models.AutoField(primary_key=True)
    raw = models.CharField(max_length=1500)
    def __str__(self):
        return str(self.UID)