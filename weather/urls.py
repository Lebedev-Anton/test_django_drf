from django.urls import include, path

urlpatterns = [
    path('v1/', include('weather.api.v1.urls')),
]
