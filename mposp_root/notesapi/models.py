from django.db import models

class Notes(models.Model): 
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    price = models.CharField(max_length=5, null=False)

def __str__(self):
    return "{} - {} - {}".format(self.title, self.description, self.price)
