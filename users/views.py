from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import *
from django.contrib.auth.models import User

# Create your views here.
class Login(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if user.is_active:
                if login_serializer.is_valid():
                    user_serializer = user_token(user)
                    extra_info = {'full_name': user_serializer.data.get('first_name') +" "+ user_serializer.data.get('last_name')}
                    data = dict(user_serializer.data, **extra_info)
                    return Response({
                        'token': login_serializer.validated_data.get('access'),
                        'refresh-token': login_serializer.validated_data.get('refresh'),
                        'user': data
                    }, status=status.HTTP_200_OK)  
                return Response({'error': 'Password or username are wrong'}, status=status.HTTP_400_BAD_REQUEST) 
            return Response({'error': 'The user is not active'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Password or username are wrong'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('id_user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Ok'}, status=status.HTTP_200_OK)
        return Response({'error': 'The user is not exist'}, status=status.HTTP_400_BAD_REQUEST)
    

class Refresh(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refreshtoken', '')
        if not refresh:
            return Response({'error': 'There is not a refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                refresh_token = RefreshToken(refresh)
                access_token = str(refresh_token.access_token)
                return Response({'token': access_token})
            
            except Exception as e:
                return Response({'error': 'Token is not valid'}, status=status.HTTP_400_BAD_REQUEST)