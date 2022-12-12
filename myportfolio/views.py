from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .models import Proyecto
from .forms import ProyectoF


from ipware import get_client_ip
from ipregister.models import IpRegister

def index(request):
    ip, is_routable = get_client_ip(request)


    if is_routable: #Si la ip Es Publica
        if request.user:
            username = request.user
        else:
            username = 'Anonymous'

        inserIP = IpRegister(user=username,ip=ip)
        inserIP.save()
    else: # IP Privada
        if request.user:
            username = request.user
        else:
            username = 'Anonymous'

        inserIP = IpRegister(user=username,ip=ip)
        inserIP.save()

    return render(request,'index.html')
    

@method_decorator(login_required, name='dispatch')
class Create_Project(View):
    def get(self, request):
        return render(request, 'proyecto.html', {'form': ProyectoF()})

    def post(self, request):
        form = ProyectoF(request.POST,request.FILES)
        if form.is_valid():
            new_proyect = form.save(commit=False)
            new_proyect.user = request.user
            new_proyect.save()
            usuario = request.user
            return redirect(f'/{usuario}')

        return render(request, 'proyecto.html', {'form': ProyectoF()})

@method_decorator(login_required, name='dispatch')
class User(View):
    def get(self,request,user):
        infouser = Proyecto.objects.filter(user_id=request.user.id)
        return render(request,'user_portafolio.html', {'infouser':infouser})

@method_decorator(login_required, name='dispatch')
class Editar(View):
    def get(self,request):
        infouser = Proyecto.objects.filter(user_id=request.user.id)
        
        return render(request,'editar.html',{'infouser':infouser})

@method_decorator(login_required, name='dispatch')
class EditarProject(View):    
    def get(self,request,project):
        # editarproject = Proyecto.objects.get(pk=project)
        editarproject = get_object_or_404(Proyecto,pk=project)
        form = ProyectoF(instance=editarproject)
        return render(request,'editarproject.html',{'editar':editarproject,'form':form})

    def post(self,request,project):
        # editarproject = Proyecto.objects.get(pk=project)
        guardar_project = get_object_or_404(Proyecto,pk=project)
        form = ProyectoF(request.POST,instance=guardar_project)
        form.save()
        return redirect('editar')
        
@login_required
def EliminarTarea(request,project):
    task = get_object_or_404(Proyecto,pk=project)
    if request.method == 'POST':
        task.delete()
        return redirect('editar')