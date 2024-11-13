from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlantSerializer
from utils.exceptions import handle_exceptions

# Model
from .models import Plant

# Create your views here.
class ListPlantView(APIView):

    # Index controller
    # Route: GET /plants/
    @handle_exceptions
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    
class RetrievePlantView(APIView):
    
    # Show controller
    # Route: GET /plants/:pk/
    @handle_exceptions
    def get(self, request, pk):
        plant = Plant.objects.get(pk=pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)