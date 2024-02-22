"""
URL configuration for scrum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf.urls.static import static
from scrumboard.views import ContactView, LogoutView,LoginView, RegistrationView, SubtaskView, TaskView, UserDefCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('contacts/', ContactView.as_view()),
    path('tasks/', TaskView.as_view()),
    path('savedCategories/', UserDefCategoryView.as_view()),
    path('subTasks/', SubtaskView.as_view()),
    path('contacts/<int:pk>/', ContactView.as_view(), name='contact-detail'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task-detail'),
    path('savedCategories/<int:pk>/', UserDefCategoryView.as_view(), name='userDefCategory-detail'),
    path('subTasks/<int:pk>/', SubtaskView.as_view(), name='subtask-detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
