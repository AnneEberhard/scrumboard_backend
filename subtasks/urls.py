from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubtaskViewSet

router = DefaultRouter()
router.register(r'subtasks', SubtaskViewSet)

urlpatterns = [
    path('', SubtaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('<int:pk>/', SubtaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-detail'),
]