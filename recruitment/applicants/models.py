from django.db import models, connection

# Create your models here.
class Applicants(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    job = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()


