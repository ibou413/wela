from django.db import models

# Create your models here.


# userapp/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):

    # Groupes et permissions
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Nom personnalisé pour éviter les conflits
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  # Nom personnalisé pour éviter les conflits
        blank=True
    )

    def __str__(self):
        return self.username
