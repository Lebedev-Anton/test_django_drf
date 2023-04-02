import requests
import datetime
from pydantic import BaseModel
from settings.settings import WEATHER_URL, WEATHER_API_KEY


class WeatherScheme(BaseModel):
    city: str
    request_date: str
    weather: str

class WeatherErrorScheme(BaseModel):
    status: str
    message: str


class Weather:
    city: str
    request_date: str

    def __init__(self, city: str, request_date: str) -> None:
        self.city = city
        self.request_date = request_date

    def validate_data(self) -> None:
        try:
            self.request_date = str(datetime.date.fromisoformat(self.request_date))
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def request_weather(self) -> WeatherScheme | WeatherErrorScheme:
        try:
            return self._request_weather()
        except ConnectionError:
            return WeatherErrorScheme(
                **{
                    'status': 'error',
                    'message': 'Connection error - Weather service not answer',
                }
            )
        except AssertionError:
            return WeatherErrorScheme(
                **{
                    'status': 'error',
                    'message': 'Weather service not answer',
                }
            )
        except (KeyError, IndexError):
            return WeatherErrorScheme(
                **{
                    'status': 'error',
                    'message': 'Weather service return incorrect answer',
                }
            )

    def _request_weather(self) -> WeatherScheme:
        response = requests.get(
            url=WEATHER_URL,
            params={
                'key': WEATHER_API_KEY,
                'q': self.city,
                'date': self.request_date,
                'format': 'json',
            }
        )

        assert response.status_code == 200

        return WeatherScheme(
            **{
            'city': self.city,
            'request_date': self.request_date,
            'weather': response.json().get('data').get('weather')[0].get('avgtempC'),
            }
        )
