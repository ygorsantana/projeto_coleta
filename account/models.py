import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from guardian.shortcuts import get_objects_for_user

# from core.models import Store, Shopping, Product, Sku
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )

    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=30,
        blank=True
    )

    last_name = models.CharField(
        max_length=30,
        blank=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_admin = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # class Meta:
    #     verbose_name = ('user')
    #     verbose_name_plural = ('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    # def allowed_stores(self):
    #     if self.is_admin or self.is_staff:
    #         return Store.objects.all()
    #     return (
    #             get_objects_for_user(self, 'core.has_store') |
    #             Store.objects.filter(shopping__in=self.allowed_shoppings())
    #     )

    # def allowed_shoppings(self):
    #     if self.is_admin or self.is_staff:
    #         return Shopping.objects.all()
    #     return get_objects_for_user(self, 'core.has_shopping')

    # def allowed_products(self):
    #     if self.is_admin or self.is_staff:
    #         return Product.objects.all()
    #     return Product.objects.filter(store__in=self.allowed_stores())

    # def allowed_skus(self):
    #     if self.is_admin or self.is_staff:
    #         return Sku.objects.all()
    #     return Sku.objects.filter(sku__in=self.allowed_products())
