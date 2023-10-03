from django.db import models

# Create your models here.
class Task(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    obs = models.CharField(max_length=255)
    #img = models.ImageField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updaated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.rua
    