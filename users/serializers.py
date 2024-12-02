from rest_framework import serializers
from users.models import User
from habits.serializers import HabitsSerializer

class UserSerializer(serializers.ModelSerializer):
    habits = HabitsSerializer(source='user_habits', many=True)
    class Meta:
        model = User
        fields = '__all__'
