from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from user.serializers import UserSerializer, UserPhotoSerializer
from user.models import User


class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if 'photo' in request.data:
                request.data.__setitem__('user', serializer.data.get('id'))
                serializer_photo = UserPhotoSerializer(data=request.data)
                if serializer_photo.is_valid():
                    serializer_photo.save()
                else:
                    return Response(serializer_photo.errors, status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserByIdAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        for key, value in request.data.items():
            setattr(user, key, value)
        user.save()
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(instance=user)
        user.delete()
        return Response(serializer.data, status.HTTP_200_OK)
