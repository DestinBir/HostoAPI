from django.db import models


class Hospital(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=300, unique=True)
    amb_number = models.CharField(max_length=13)
    specialities = models.CharField(max_length=500)
    logo = models.ImageField()

    def get_specialities(self):
        s = self.specialities.split(',')
        return s

    def __str__(self):
        return self.name


