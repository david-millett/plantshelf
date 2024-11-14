from django.db import models

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=40)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    bio = models.TextField()
    light = models.CharField(max_length=20)
    is_toxic = models.BooleanField(default=False)
    difficulty = models.CharField(max_length=20)
    water_interval = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.common_name} ({self.genus} {self.species})'