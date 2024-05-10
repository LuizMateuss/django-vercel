from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializer import UserSerializer, CustomTokenObtainPairSerializer
from .decorators import jwt_auth_required

@jwt_auth_required
def _token_get_claims(token):
    return token.jwt_payload

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def list(self, request, **kwargs):
        """Exibindo usuario"""
        payload = _token_get_claims(request)
        user_id = payload['user_id']

        queryset = User.objects.filter(id=user_id).first()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer