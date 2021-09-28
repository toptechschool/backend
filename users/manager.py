from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **kwargs):
        if email is None:
            raise TypeError("Must provide email")
        if password is None:
            raise TypeError("Must provide password")

        email = self.normalize_email(email)
        is_staff = kwargs.pop('is_staff', False)
        is_superuser = kwargs.pop('is_superuser', False)
        is_approved = kwargs.pop('is_approved',False)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_approved=is_approved,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, is_staff=False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_staff=True, is_superuser=True,is_approved=True, **extra_fields)