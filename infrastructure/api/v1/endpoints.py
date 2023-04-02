from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from infrastructure.servises.monitoring import MemoryMonitoring


@api_view(['GET'])
def monitoring_process_memory(request: Request) -> Response:
    return Response(MemoryMonitoring.get_process_memory_info().dict(), status=status.HTTP_200_OK)


@api_view(['GET'])
def monitoring_full_memory(request: Request) -> Response:
    return Response(MemoryMonitoring.get_full_memory_info().dict(), status=status.HTTP_200_OK)