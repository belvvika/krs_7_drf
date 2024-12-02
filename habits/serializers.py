from rest_framework import serializers

from habits.validators import SimultaneousSelectionValidator, AssociatedAndNiceValidator, time_validator
from habits.models import Habits

class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        validators = [
            SimultaneousSelectionValidator('reward', 'associated_habit', 'sign_of_nice_habit'),
            AssociatedAndNiceValidator('associated_habit'),
            time_validator
        ]

class HabitsDetailSerializer(serializers.ModelSerializer):
    model = Habits
    fields = '__all__'