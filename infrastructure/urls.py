from django.urls import path, include

urlpatterns = [
    path('v1/', include('infrastructure.api.v1.urls')),
]
