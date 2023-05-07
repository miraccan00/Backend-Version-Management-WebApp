from django.db import models

class ReleaseProject1(models.Model):
    date = models.DateField()
    release_artifact = models.CharField(max_length=100)
    release_number = models.CharField(max_length=50)
    release_path = models.CharField(max_length=100)
    service_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    microui = models.BooleanField()
    sql = models.BooleanField()
    uat = models.BooleanField()
    prod = models.BooleanField()
    

    def __str__(self):
        return f"{self.service_name} {self.version} ({self.release_number})"