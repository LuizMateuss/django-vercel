from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import UserViewSet, CustomTokenObtainPairView

urlpatterns = [
    path('tokens/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tokens/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('users/', UserViewSet.as_view({'get': 'list'}), name='users'),
]