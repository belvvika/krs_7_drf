from django.urls import path
from rest_framework.routers import DefaultRouter
from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, HabitsListApiView, HabitsUpdateApiView, HabitsDestroyApiView, HabitsRetrieveApiView, HabitsCreateApiView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register('', HabitsViewSet)

urlpatterns = [
    path('habits/', HabitsListApiView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', HabitsRetrieveApiView.as_view(), name='habits_retrieve'),
    path('habits/create/', HabitsCreateApiView.as_view(), name='habits_create'),
    path('habits/<int:pk>/update/', HabitsUpdateApiView.as_view(), name='habits_update'),
    path('habits/<int:pk>/delete/', HabitsDestroyApiView.as_view(), name='habits_delete'),
] + router.urls

