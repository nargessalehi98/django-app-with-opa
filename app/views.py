from django.http import JsonResponse
from rest_framework import status
from app.models import CustomUser
from app.serializers import UserSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from config.messages import USER_ADDED


class AccessTokenObtainView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Remove the refresh token from the response
        del response.data['refresh']
        return response


class UserAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        users = self.get_queryset().values("name", "email")
        return JsonResponse({"users": list(users)}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
        return JsonResponse(data=USER_ADDED, status=status.HTTP_201_CREATED)
