from django.conf import settings
from django.db import models


class Role(models.Model):
    DATA_ENTRY = "data_entry"
    ADMIN = "admin"
    ROLE_CHOICES = [
        (DATA_ENTRY, "Data Entry"),
        (ADMIN, "Admin"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=63, choices=ROLE_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "role"], name="unique_user_role"),
        ]
