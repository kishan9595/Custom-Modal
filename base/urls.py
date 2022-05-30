
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="home"),
    path('loginuser/', loginuser, name='loginuser'),
    path('registerUser/', registerUser, name='registerUser'),
    path('createuser/', createUser, name="createuseer"),

    path('updateuser/<str:pk>/', updateUser, name="updateuser"),

    path('deleteuser/<str:pk>/', deleteUser, name="deleteuser"),
]
