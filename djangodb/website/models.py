from django.db import models

class Members(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.EmailField(max_length=200)
    age=models.CharField(max_length=200)
    balance=models.IntegerField()
class Histor(models.Model):
    ForWhatYouSpent=models.CharField(max_length=200)
    spend=models.IntegerField()