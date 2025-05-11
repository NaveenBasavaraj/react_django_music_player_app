from django.urls import path
from api.views import RoomView

urlpatterns = [
    path('rooms/', RoomView.as_view(), name='RoomView'),
]
