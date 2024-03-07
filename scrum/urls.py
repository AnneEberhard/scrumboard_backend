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
from django.urls import path, include
from django.conf.urls.static import static
from scrumboard.views import ContactAtRegisterView, LoginView, ForgotView, LogoutView, PasswordResetConfirmView, RegistrationView
from categories import urls as categories_urls
from tasks import urls as tasks_urls
from contacts import urls as contacts_urls
from subtasks import urls as subtasks_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('contacts/', include(contacts_urls)),
    path('tasks/', include(tasks_urls)),
    path('categories/', include(categories_urls)),
    path('subTasks/', include(subtasks_urls)),
    path('forgot/', ForgotView.as_view()),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('contacts-at-register/', ContactAtRegisterView.as_view(), name='contacts-at-register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
