
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name="home"),
    path('loginuser/', loginuser, name='loginuser'),
    path('registerUser/', registerUser, name='registerUser'),
    path('alluser/', alluser, name='alluser'),
    path('logoutuser/', logoutUser, name="logoutuser"),
    path('createuser/', createUser, name="createuseer"),

    path('updateuser/<str:id>/', updateUser, name="updateuser"),

    path('singleuser/<str:id>/', singleuser, name="singleuser"),
]
