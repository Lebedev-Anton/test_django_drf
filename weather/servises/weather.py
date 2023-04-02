import requests
import datetime

from settings.settings import WEATHER_URL, WEATHER_API_KEY


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

    def request_weather(self) -> dict:
        try:
            return self._request_weather()
        except ConnectionError:
            return {
                'status': 'error',
                'message': 'Connection error - Weather service not answer',
            }
        except AssertionError:
            return {
                'status': 'error',
                'message': 'Weather service not answer',
            }
        except (KeyError, IndexError):
            return {
                'status': 'error',
                'message': 'Weather service return incorrect answer',
            }

    def _request_weather(self) -> dict:
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

        return {
            'city': self.city,
            'request_date': self.request_date,
            'weather': response.json().get('data').get('weather')[0].get('avgtempC'),
        }
