from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q


# Model
from django.contrib.auth import get_user_model, hashers
User = get_user_model()

# Create your views here.
class SignUpView(APIView):

# ! Add erro handling

    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        created_user = new_user.save()

        token_pair = RefreshToken.for_user(created_user)

        return Response({
            'message': 'Signup successful',
            'user': new_user.data,
            'token': str(token_pair.access_token)
        })
    
class SignInView(APIView):

    def post(self, request):

        u_or_e = request.data.get('username_or_email')
        password = request.data.get('password')

        # Find the user with matching username or email
        user = User.objects.get(Q(username=u_or_e) | Q(email=u_or_e))

        # Check plain text password from request body against stored hash
        if hashers.check_password(password, user.password):
            # Generate token using simpleJWT
            token_pair = RefreshToken.for_user(user)

            serialized_user = UserSerializer(user)

            return Response({
                'user': serialized_user.data,
                'token': str(token_pair.access_token)
            })
        
        # Send 401 if passwords don't match
        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)