from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # JWT token views
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get JWT tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT tokens
]
