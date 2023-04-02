from django.urls import path
from user.api.v1.endpoints import UserAPIView, UserByIdAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('user/<int:user_id>', UserByIdAPIView.as_view()),
]
