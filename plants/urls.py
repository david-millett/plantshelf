from django.urls import path
from .views import ListPlantView, RetrievePlantView

# Every request that hits this file starts with /plants

urlpatterns = [
    path('', ListPlantView.as_view()),
    path('<int:pk>/', RetrievePlantView.as_view())
]