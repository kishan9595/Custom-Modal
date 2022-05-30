from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager 

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, mobile,email,  password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not mobile:
            raise ValueError('The given mobile must be set')

        user = self.model(mobile=mobile, email=email, **extra_fields)
        if password:
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self,mobile, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(mobile, email, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(mobile, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    mobile = models.CharField(max_length = 12, unique=True)
    password = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return self.mobile
        
    # def has_perm(self, perm, obj=None):
    #     if self.is_adm and isinstance(obj, User):
    #         return True
    #     return super().has_perm(perm, obj)    