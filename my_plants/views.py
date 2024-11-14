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
    
# ! Need to dynamically add user ID

    # Create contoller
    # Route: POST /my_plants/
    @handle_exceptions
    def post(self, request):
        my_new_plant = MyPlantSerializer(data=request.data)
        my_new_plant.is_valid(raise_exception=True)
        my_new_plant.save()
        return Response(my_new_plant.data, status.HTTP_201_CREATED)

class RetrieveUpdateDestroyMyPlantView(APIView):
    
    # Show controller
    # Route: GET /my_plants/:pk/
    @handle_exceptions
    def get(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        serializer = MyPlantSerializer(my_plant)
        return Response(serializer.data)
    
    # Delete controller
    # Route: DELETE /my_plants/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        my_plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Update controller
    # Route: PUT /my_plants/:pk/
    @handle_exceptions
    def put(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        serializer = MyPlantSerializer(my_plant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
