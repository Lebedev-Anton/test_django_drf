from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from user.serializers import UserSerializer
from user.models import User
from user.api.v1.schemas import request_body, response, errors
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            200: openapi.Schema(type=openapi.TYPE_ARRAY, items=response)
        }
    )
    def get(self, request: Request) -> Response:
        """Запрос информации о всех пользователях."""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=request_body,
        responses={
            201: response,
            400: errors,
        }
    )
    def post(self, request: Request) -> Response:
        """Регистрация пользователя."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserByIdAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=request_body,
        responses={
            201: response,
            404: errors,
        }
    )
    def put(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        for key, value in request.data.items():
            setattr(user, key, value)
        user.save()
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=request_body,
        responses={
            201: response,
            404: errors,
        }
    )
    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(instance=user)
        user.delete()
        return Response(serializer.data, status.HTTP_200_OK)
