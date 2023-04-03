from drf_yasg import openapi

request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='first name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='last name'),
        'birthday': openapi.Schema(type=openapi.TYPE_STRING, description='birthday'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, description='gender'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
        'photo': openapi.Schema(type=openapi.TYPE_STRING, description='photo'),
    },
)

response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='first name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='last name'),
        'birthday': openapi.Schema(type=openapi.TYPE_STRING, description='birthday'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, description='gender'),
        'photo': openapi.Schema(type=openapi.TYPE_STRING, description='photo'),
    },
)

errors = openapi.Schema(type=openapi.TYPE_OBJECT, description='Errors')
