
from django.db import models
from django.contrib.auth.models import AbstractUser

from guitarradar.utils.models import BaseModel


class User(AbstractUser, BaseModel):

    class AdminLevels(models.TextChoices):
        NOT_ADMIN = 'NA', 'user'
        ADMIN = 'AD', 'admin'
        MASTER_ADMIN = 'MA', 'master admin'
        FOUNDER = 'FO', 'founder'

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    admin_level = models.CharField(
        max_length=2, choices=AdminLevels.choices, default='NA'
    )

    @property
    def is_admin(self) -> bool:
        return str(self.admin_level) \
               and self.admin_level != User.AdminLevels.NOT_ADMIN

    def __str__(self):
        return self.username
