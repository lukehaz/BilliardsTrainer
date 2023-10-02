from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="@.com")
    password = models.CharField(max_length=20, default="/")

    
    def __str__(self):
        return self.username

class Stats(models.Model):
    userStats = models.ForeignKey(User, on_delete=models.CASCADE)
    drillsComplete = models.IntegerField(default=0)
    

    def __int__(self):
        return self.drillsComplete

