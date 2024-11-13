from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Location
from .serializers import LocationSerializer

# Create your views here.
class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer