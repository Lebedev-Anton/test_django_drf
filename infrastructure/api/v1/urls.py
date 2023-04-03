from django.urls import path

from infrastructure.api.v1.endpoints import (monitoring_full_memory,
                                             monitoring_process_memory)

urlpatterns = [
    path('infrastructure/full/', monitoring_full_memory),
    path('infrastructure/process/', monitoring_process_memory),
]
