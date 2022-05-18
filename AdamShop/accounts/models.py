from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    MALE = 'Mr.'
    FEMALE = 'Mrs.'
    GENDER = [
        (MALE, 'Mr.'),
        (FEMALE, 'Mrs'),
    ]
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    first_name = models.CharField(max_length=25, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=35, blank=True, null=True, verbose_name='Last name')
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=55, blank=True, null=True, verbose_name='Country')
    city = models.CharField(max_length=55, blank=True, null=True, verbose_name='City')
    state = models.CharField(max_length=55, blank=True, null=True, verbose_name='State')
    zip_code = models.IntegerField('Zip code', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
