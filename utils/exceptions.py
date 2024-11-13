from rest_framework.response import Response
from rest_framework import status
from plants.models import Plant

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Plant.DoesNotExist as e:
            print(e)
            return Response({ 'detail': str(e) }, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            print('Error name:', e.__class__.__name__)
            return Response({ 'detail': 'An unknown error occurred' }, status.HTTP_500_INTERNAL_SERVER_ERROR)
    return wrapper