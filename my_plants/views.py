from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import MyPlantSerializer, PopulatedMyPlantSerializer
from utils.exceptions import handle_exceptions
from utils.permissions import IsOwner

# Model
from .models import My_plant

# Create your views here.
class ListCreateMyPlantView(APIView):
    permission_classes=[IsAuthenticated]

# Index route is filtered so that only their own plants show up

    # Index controller
    # Route: GET /my_plants/
    @handle_exceptions
    def get(self, request):
        my_plants = My_plant.objects.select_related('species', 'owner', 'location').filter(owner=request.user.id)
        serialzer = PopulatedMyPlantSerializer(my_plants, many=True)
        return Response(serialzer.data)
    
    # Create contoller
    # Route: POST /my_plants/
    @handle_exceptions
    def post(self, request):
        request.data['owner'] = request.user.id
        my_new_plant = MyPlantSerializer(data=request.data)
        my_new_plant.is_valid(raise_exception=True)
        my_new_plant.save()
        return Response(my_new_plant.data, status.HTTP_201_CREATED)

class RetrieveUpdateDestroyMyPlantView(APIView):
    permission_classes=[IsOwner]
    
    # Show controller
    # Route: GET /my_plants/:pk/
    @handle_exceptions
    def get(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        self.check_object_permissions(request, my_plant)
        serializer = PopulatedMyPlantSerializer(my_plant)
        return Response(serializer.data)
    
    # Delete controller
    # Route: DELETE /my_plants/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        self.check_object_permissions(request, my_plant)
        my_plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Update controller
    # Route: PUT /my_plants/:pk/
    @handle_exceptions
    def put(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        self.check_object_permissions(request, my_plant)
        serializer = MyPlantSerializer(my_plant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # Update patch controller
    # Route: PATCH /my_plants/:pk/
    @handle_exceptions
    def patch(self, request, pk):
        my_plant = My_plant.objects.get(pk=pk)
        self.check_object_permissions(request, my_plant)
        serializer = MyPlantSerializer(my_plant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
