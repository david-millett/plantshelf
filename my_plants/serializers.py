from rest_framework.serializers import ModelSerializer
from .models import My_plant
from plants.serializers import PlantSerializer
from users.serializers import UserSerializer
from locations.serializers import LocationSerializer

class MyPlantSerializer(ModelSerializer):
    class Meta:
        model = My_plant
        fields = '__all__'

class PopulatedMyPlantSerializer(MyPlantSerializer):
    species = PlantSerializer()
    owner = UserSerializer()
    location = LocationSerializer()