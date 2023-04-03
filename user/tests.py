from django.test import TestCase
from user.models import User
from faker import Faker


class UserOperationTest(TestCase):
    refresh_token: str
    access_token: str

    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        user = User.objects.create_user(
            email='fake@mail.ru',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender='m',
            password='12345678',
        )
        user.save()

    def setUp(self):
        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/token/',
            data={
                'email': 'fake@mail.ru',
                'password': '12345678',
            }
        )

        self.refresh_token = response.data.get('refresh')
        self.access_token = response.data.get('access')

    def test_get_all_users(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/user/',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )

        user = User(**response.data[0])

        self.assertEqual(user.email, 'fake@mail.ru')
        self.assertEqual(user.gender, 'm')

    def test_create_new_user(self):
        fake = Faker()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()

        response = self.client.post(
            'http://127.0.0.1:8000/api/v1/user/',
            data={
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'gender': 'm',
                'password': '12345678',
            },
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )

        user = User(**response.data)

        self.assertEqual(user.pk, 2)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.gender, 'm')

    def test_update_user(self):
        fake = Faker()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()

        response = self.client.put(
            'http://127.0.0.1:8000/api/v1/user/1',
            data={
                'email': email,
            },
            content_type='application/json',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )
        user = User(**response.data)

        self.assertNotEqual(user.email, 'fake@mail.ru')
        self.assertEqual(user.pk, 1)

        response = self.client.put(
            'http://127.0.0.1:8000/api/v1/user/1',
            data={
                'first_name': first_name,
                'last_name': last_name,
            },
            content_type='application/json',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )
        user = User(**response.data)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

        response = self.client.put(
            'http://127.0.0.1:8000/api/v1/user/2',
            data={
                'email': email,
            },
            content_type='application/json',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )

        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        response = self.client.delete(
            'http://127.0.0.1:8000/api/v1/user/2',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )
        self.assertEqual(response.status_code, 404)

        response = self.client.delete(
            'http://127.0.0.1:8000/api/v1/user/1',
            **{
                'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'
            }
        )

        user = User(**response.data)
        self.assertEqual(user.pk, None)
