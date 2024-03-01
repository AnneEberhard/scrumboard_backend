from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-detail'),
]