from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from atendimento import urls as atendimento_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LogoutView.as_view(), name='logout'),
    path('paciente/', include(atendimento_urls)),
]
