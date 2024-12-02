from datetime import timedelta

from rest_framework.validators import ValidationError


class SimultaneousSelectionValidator:
    def __init__(self, reward, associated_habit, sign_of_nice_habit):
        self.reward = reward
        self.associated_habit = associated_habit
        self.sign_of_nice_habit = sign_of_nice_habit

    def __call__(self, value):
        reward_field = value.get(self.reward)
        associated_habit_field = value.get(self.associated_habit)
        sign_of_nice_habit_field = value.get(self.sign_of_nice_habit)

        if reward_field and associated_habit_field:
            raise ValidationError(
                "Может быть заполнено поле reward или поле associated_habit"
            )
        if sign_of_nice_habit_field:
            if reward_field or associated_habit_field:
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )
        else:
            if not reward_field and not associated_habit_field:
                raise ValidationError(
                    "Поле reward или поле associated_habit обязательно для заполнения у полезной привычки"
                )

class AssociatedAndNiceValidator:
    def __init__(self, associated_habit):
        self.associated_habit = associated_habit

    def __call__(self, value):
        associated_habit_field = value.get(self.associated_habit)

        if associated_habit_field:
            if not value.get('sign_of_nice_habit'):
                raise ValidationError(
                    "У связанной привычки должен быть признак хорошей привычки"
                )

def time_validator(value):
    if value:
        if value > timedelta(seconds=120):
            raise ValidationError(
                "Время выполнения привычки не может превышать 2 минуты"
            )
