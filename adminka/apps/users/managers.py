from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CustomUserManager(UserManager):
    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Provide correct email address")

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Provide an email address")
        else:
            self.validate_email(email)

        if not password:
            raise ValueError("Provide a password")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if not extra_fields.get("is_staff"):
            raise ValueError("Super user must be staff")
        user = self.create_user(email, password, **extra_fields)
        user.save()
        return user
