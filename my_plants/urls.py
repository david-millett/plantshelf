from django.urls import path
from .views import ListCreateMyPlantView, RetrieveUpdateDestroyMyPlantView

# Every request that hits this file starts with /my_plants

urlpatterns = [
    path('', ListCreateMyPlantView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyMyPlantView.as_view())
]