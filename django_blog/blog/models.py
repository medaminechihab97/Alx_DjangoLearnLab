from django.db import models
from django.contrib.auth.models import User , AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique= True) 
    def __str__(self):
        return self.username
    
class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts', null=True)