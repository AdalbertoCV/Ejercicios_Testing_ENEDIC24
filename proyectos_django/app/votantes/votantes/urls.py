from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from candidatos.views import lista_candidatos

urlpatterns = [
    path('', lista_candidatos, name='ListaCandidatos'),
    path('admin/', admin.site.urls),
    path('Candidatos/', include('candidatos.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)