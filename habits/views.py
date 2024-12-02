
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from habits.models import Habits
from habits.serializers import HabitsSerializer, HabitsDetailSerializer
from habits.paginations import CustomPagination
from users.permissions import IsOwner



class HabitsViewSet(ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return HabitsDetailSerializer
        return HabitsSerializer

    def get_permissions(self):
        if self.action in ["retrieve", "update", "destroy"]:
            self.permission_classes = [IsOwner | IsAdminUser]
        return super().get_permissions()

class HabitsCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

class HabitsListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = CustomPagination

class HabitsRetrieveApiView(RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)

class HabitsUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)

class HabitsDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)
