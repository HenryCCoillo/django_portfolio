from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Proyecto(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    url = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="user",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
