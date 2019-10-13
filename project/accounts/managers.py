
from allauth.account.models import EmailAddress

from django.contrib.auth.models import (
    BaseUserManager,
)


class UserManager(BaseUserManager):

    def get_by_natural_key(self, username: str):
        return self.get(email__iexact=username)

    def create_user(self, email: str, password: str):
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
    
        EmailAddress.objects.create(user=user, email=email, verified=True, primary=True)
    
        return user
