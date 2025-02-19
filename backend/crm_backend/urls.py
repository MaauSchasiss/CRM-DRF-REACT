from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importar las vistas de cada app
from client.views import ClientViewSet
from leads.views import LeadViewSet
from users.views import UserViewSet
from product.views import ProductViewSet

# Crear un solo router para TODAS las APIs
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'users', UserViewSet)
router.register(r'product', ProductViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/', permanent=True)),
    path('api/', include(router.urls)),  # Un solo include para todas las rutas
]