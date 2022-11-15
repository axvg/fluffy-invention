from django.db.models import CharField
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = CharField(null=True, blank=True, max_length=100)
