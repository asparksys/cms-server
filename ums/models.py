from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

from club.models import BranchClub


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("invalid email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    # fields
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=255, null=True)
    club_id = models.ForeignKey(
        BranchClub, blank=True, null=True, on_delete=models.CASCADE, default=None
    )
    admin = models.BooleanField(default=False)  # access django admin site
    active = models.BooleanField(default=True)
    user_image = models.URLField(max_length=2048, default="https://picsum.photos/200")
    # configs
    USERNAME_FIELD = "email"  # overwrite the built-in username field w/ email
    # email & password are required by default, revisit to add extra required fields
    REQUIRED_FIELDS = []

    # methods
    def __str__(self):
        return self.email

    def has_perm(self, obj=None):
        return self.admin

    def has_module_perms(self, obj=None):
        return self.admin

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.admin

    @property
    def location(self):
        return self.address
