from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils import timezone


class CustomUser(AbstractUser):         
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_authorized = models.BooleanField(default=False)
    login_token = models.CharField(max_length=6, blank=True, null=True)

    # prevent reverse conflict
    groups = models.ManyToManyField(
        'auth.Group',
        related_name=None,
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name=None,
        blank=True
    )

    def __str__(self):
        return self.email


def generate_token():
    return get_random_string(64)


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default=generate_token, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    TOKEN_VALIDITY_PERIOD = timezone.timedelta(hours=1)

    def is_valid(self):
        return timezone.now() <= self.created_at + self.TOKEN_VALIDITY_PERIOD

    def send_reset_email(self):
        reset_link = f"{settings.DOMAIN}/reset-password/{self.token}/"

        send_mail(
            'Password Reset Request',
            f'Hi,\n\nClick the link to reset your password:\n{reset_link}\n\nThis link will expire in 1 hour.',
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
            fail_silently=False,
        )