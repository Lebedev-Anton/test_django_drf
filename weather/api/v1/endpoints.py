from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from weather.servises.weather import Weather


@api_view(['GET'])
def get_weather(request: Request, city: str, request_date: str) -> Response:
    weather = Weather(city=city, request_date=request_date)
    try:
        weather.validate_data()
    except ValueError as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    response = weather.request_weather()

    if 'status' in response:
        response_status = status.HTTP_400_BAD_REQUEST
    else:
        response_status = status.HTTP_200_OK

    return Response(response, status=response_status)
