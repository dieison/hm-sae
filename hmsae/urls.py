from django.contrib import admin
from django.urls import path, include
from atendimento import urls as atendimento_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('paciente/', include(atendimento_urls)),
]
