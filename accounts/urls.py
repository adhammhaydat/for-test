from django.urls import path
from .views import RegisterView,PhotoDetail
#  LogoutAPIView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)