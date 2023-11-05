

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer, UserDetailSerializer,PhoneLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User




class PhoneLoginView(APIView):
    def post(self, request):
        serializer = PhoneLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'access_token': access_token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create_user()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_201_CREATED)



class GetUserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_details = {
            "username": user.username,
            "email": user.email,
            "userid":user.id
            # Add more user details as needed
        }
        return Response(user_details, status=status.HTTP_200_OK)