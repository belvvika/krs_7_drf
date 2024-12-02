from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        help_text='Введите вашу электронную почту'
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name='Номер телефона',
        help_text='Введите ваш номер телефона'
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Город',
        help_text='Введите ваш город'
    )
    tg_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='ID Telegram',
        help_text='Введите ID Telegram пользователя'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email