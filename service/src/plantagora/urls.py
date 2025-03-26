from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.api import CreateProfileRestView, GetUserUsernameRestView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api/getUserUsername/', GetUserUsernameRestView.as_view(), name="getUserUsernameRestView"),

]

router = DefaultRouter(trailing_slash=False)
router.register('api/register/',CreateProfileRestView, basename='CreateProfileRestView')

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)