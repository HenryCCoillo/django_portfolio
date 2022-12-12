from django.db import models

class IpRegister(models.Model):
    user = models.CharField(max_length=20)
    ip =  models.CharField(max_length=20)
    ip_register = models.DateTimeField(auto_now_add=True)