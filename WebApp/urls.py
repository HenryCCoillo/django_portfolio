
from django.contrib import admin
from django.urls import path, include

from autenticacion.views import VRegistro,cerrar_sesion,logear

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myportfolio.urls'),name='Home'),
    

    #Autenticacion
    path('register/',VRegistro.as_view(),name="register"),
    path('login/',logear,name="login"),
    path('exit/',cerrar_sesion,name="exit"),

    #IP Register
    path('ip/', include('ipregister.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

