from django.test import TestCase
from weather.servises.weather import Weather, WeatherScheme
from settings.settings import WEATHER_API_KEY


class TestWeatherRequest(TestCase):

    def test_weather(self):
        weather = Weather('Moskwa', '2009-07-21')
        weather.validate_data()
        response = weather.request_weather()
        self.assertTrue(hasattr(response, 'city'))
        self.assertTrue(hasattr(response, 'request_date'))
        self.assertTrue(hasattr(response, 'weather'))

        weather = Weather('Moskwa', '2009-07-212')
        try:
            weather.validate_data()
        except ValueError as e:
            self.assertEqual(str(e), 'Incorrect data format, should be YYYY-MM-DD')


class TestWeatherApi(TestCase):

    def test_weather_api(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/weather/Moskwa/2009-07-21/',
            **{
                'key': WEATHER_API_KEY,
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('city'), 'Moskwa')
        self.assertTrue('request_date' in response.data)
        self.assertTrue('weather' in response.data)

        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/weather/Murom/2019-12-21/',
            **{
                'key': WEATHER_API_KEY,
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('city'), 'Murom')
        self.assertTrue('request_date' in response.data)
        self.assertTrue('weather' in response.data)
