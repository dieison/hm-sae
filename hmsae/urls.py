from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from home import urls as home_urls
from atendimento import urls as atendimento_urls



urlpatterns = [
    path('', include(home_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('paciente/', include(atendimento_urls)),
]
