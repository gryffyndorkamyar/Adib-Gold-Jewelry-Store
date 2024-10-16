from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    national_code = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)],verbose_name="کد ملی")


    def __str__(self) -> str:
        return self.username