from django.db import models

class Habits(models.Model):
    habit = models.CharField(
        max_length=100,
        verbose_name='Название привычки',
        help_text='Введите название вашей привычки'
    )
    place = models.CharField(
        max_length=100,
        verbose_name='Место выполнения',
        help_text='Введите место выполнения вашей привычки',
        blank=True,
        null=True
    )
    time = models.TimeField(
        verbose_name='Время',
        help_text='Введите время, когда будет вцыполнятся ваша привычка',
        blank=True,
        null=True
    )
    sign_of_nice_habit = models.BooleanField(
        verbose_name='Признак хорошей привычки',
        help_text='Укажите, является ли ваша привычка хорошей',
        default=False
    )
    associated_habit = models.ForeignKey(
        'Habits',
        on_delete=models.CASCADE,
        verbose_name='Связанная привычка',
        help_text='Выберите связанную привычку',
        blank=True,
        null=True
    )
    periodicity = models.CharField(
        max_length=100,
        verbose_name='Периодичность выполнения',
        help_text='Введите периодичность выполнения вашей привычки',
        choices=[
            ('daily', 'Ежедневно'),
            ('weekly', 'Еженедельно'),
            ('monthly', 'Ежемесячно'),
            ('yearly', 'Ежегодно')
        ],
        default='daily'
    )
    reward = models.CharField(
        max_length=100,
        verbose_name='Награда за выполнение',
        help_text='Введите награду за выполнение вашей привычки',
        blank=True,
        null=True
    )
    time_to_complete = models.TimeField(
        verbose_name='Время выполнения',
        help_text='Введите время выполнения вашей привычки',
        blank=True,
        null=True
    )
    sign_of_publicity = models.CharField(
        max_length=100,
        verbose_name='Признак публичности',
        help_text='Введите признак публичности вашей привычки',
        choices=[
            ('yes', 'Да'),
            ('no', 'Нет')
        ],
        default='no'
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец привычки',
        help_text='Выберите владельца вашей привычки'
    )

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return self.habit