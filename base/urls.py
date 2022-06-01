
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="home"),
    path('loginuser/', loginuser, name='loginuser'),
    path('registerUser/', registerUser, name='registerUser'),
    path('alluser/', alluser, name='alluser'),
    path('logoutuser/', logoutUser, name="logoutuser"),
    path('createuser/', createuser, name="createuser"),
    path('deleteuser/<str:id>/', deleteuser, name="deleteuser"),
    path('updateuser/<str:id>/', updateuser, name="updateuser"),

    path('singleuser/<str:id>/', singleuser, name="singleuser"),
]
