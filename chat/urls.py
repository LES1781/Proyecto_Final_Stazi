from django.urls import path

from . import views

urlpatterns = [
    path('room_list/', views.RoomList.as_view(), name='room_list'),
    path('room_create/', views.RoomCreate.as_view(), name='room_create'),
    path('<slug:slug>/', views.room_detail, name='room_detail'),
]
