from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    """Default User model with UUID as id"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
