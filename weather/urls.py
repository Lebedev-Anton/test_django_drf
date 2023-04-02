from django.urls import path, include

urlpatterns = [
    path('v1/', include('weather.api.v1.urls')),
]
