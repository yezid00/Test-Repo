from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from project.accounts.managers import UserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.email

    @property
    def is_staff(self) -> bool:
        return self.is_superuser

    def get_short_name(self) -> str:
        return self.email

