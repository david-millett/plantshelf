from rest_framework.serializers import ModelSerializer
from .models import My_plant

class MyPlantSerializer(ModelSerializer):
    class Meta:
        model = My_plant
        fields = '__all__'