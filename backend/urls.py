from django.urls import path, include

urlpatterns = [
    # ... existing code ...
    path('api/', include('leads.urls')),
    # ... existing code ...
] 