from celery import shared_task
from habits.models import Habits
from habits.services import send_message

@shared_task
def send_message_to_user():
    habits = Habits.objects.all()
    for habit in habits:
        send_message(f'Ваша цель: {habit.title}. Время: {habit.time}', habit.user.telegram_id)
