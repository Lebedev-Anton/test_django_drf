from django.urls import path
from weather.api.v1.endpoints import get_weather

urlpatterns = [
    path('weather/<str:city>/<str:request_date>/', get_weather),
]
