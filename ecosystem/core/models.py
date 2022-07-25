from django.db import models

class Message(models.Model):
    myemail = models.EmailField()
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
   

    def __str__(self):
        return self.myemail