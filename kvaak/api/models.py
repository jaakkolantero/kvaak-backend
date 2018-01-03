from django.db import models
from django.core.validators import MinValueValidator


class Species(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sighting(models.Model):
    date_time = models.DateTimeField()
    description = models.TextField(max_length=500)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.species.name + " " + str(self.date_time)
