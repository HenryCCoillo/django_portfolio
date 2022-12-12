from django.urls import path
from .views import index, Create_Project,User,Editar,EditarProject,EliminarTarea

urlpatterns = [
    path('',index,name="Home"),
    path('crear/',Create_Project.as_view(),name="create"),
    path('<user>',User.as_view(),name="usuario"),
    path('editar/',Editar.as_view(),name="editar"),
    path('editar/<project>/',EditarProject.as_view(),name="ediarprojecto"),
    path('editar/<project>/eliminar/',EliminarTarea,name="eliminarprojecto"),
]
