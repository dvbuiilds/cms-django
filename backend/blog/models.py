from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from users.models import author


class Post(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    author_id = models.ForeignKey(to= author, on_delete=models.CASCADE, default= 1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    header_image = models.ImageField(null=True , blank=True,upload_to="images/")
    img_caption = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'id':self.id})    

    
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%s - %s' % (self.post.title , self.name)
