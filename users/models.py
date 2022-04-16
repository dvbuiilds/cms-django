from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class author(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phno = models.CharField(max_length=20)
    image = models.ImageField(default='images/default.jpg', upload_to='static/profile_pics')

    def __str__(self):
        return f'{self.username} Profile'
    
    @staticmethod
    def get_auth_by_username(_username):
        try:
            return author.objects.get(username = _username)
        except:
            return False