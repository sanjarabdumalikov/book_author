# Create your models here.
from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('s','author'),
        ('t','book')
    )

    USERNAME_FIELD = 'username'
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class authorModel(models.Model):
    name = models.CharField(max_length=65, default='')
    fname = models.CharField(max_length=65, default='')
    date_of_birth = models.DateField(default=datetime.now)
    country = models.CharField(max_length=15, default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'


class bookcategoryModel(models.Model):
    name = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book_category'


class bookModel(models.Model):
    author = models.ForeignKey(authorModel, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=127, default='')
    category = models.ForeignKey(bookcategoryModel, on_delete=models.SET_NULL, null=True)
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    image = models.ImageField(upload_to='upload/bookModel')
    yers = models.CharField(max_length=15,default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book'