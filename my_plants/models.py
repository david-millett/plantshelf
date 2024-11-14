from django.db import models

# Create your models here.
class My_plant(models.Model):
    nickname = models.CharField(max_length=40)
    species = models.ForeignKey(
        to='plants.Plant',
        related_name='individual_plants',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        to='users.User',
        related_name='plant_collection',
        on_delete=models.CASCADE
    )
    height = models.PositiveIntegerField(blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
    location = models.ForeignKey(
        to='locations.Location',
        related_name='contains',
        on_delete=models.CASCADE
    )
    last_watered = models.DateField(blank=True, null=True)
    added_on = models.DateField(auto_now_add=True)
    # updates =

    def __str__(self):
        return self.nickname