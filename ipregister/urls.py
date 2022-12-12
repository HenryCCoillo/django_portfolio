from django.urls import path
from .views import index
# proyectoPor
urlpatterns = [
    path('',index,name="ip"),
]
