from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyPlantSerializer
from utils.exceptions import handle_exceptions

# Model
from .models import My_plant

# Create your views here.
class ListCreateMyPlantView(APIView):

# ! Will want to filter this to only bring up their own

    # Index controller
    # Route: GET /my_plants/
    @handle_exceptions
    def get(self, request):
        my_plants = My_plant.objects.all()
        serialzer = MyPlantSerializer(my_plants, many=True)
        return Response(serialzer.data)
    
    # Create contoller
    # Route: POST /my_plants/
    @handle_exceptions
    def post(self, request):
        my_new_plant = MyPlantSerializer(data=request.data)
        my_new_plant.is_valid(raise_exception=True)
        my_new_plant.save()
        return Response(my_new_plant.data, status.HTTP_201_CREATED)

class RetrieveUpdateDestroyMyPlantView(APIView):
    pass