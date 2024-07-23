from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    date_born = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return self.username
