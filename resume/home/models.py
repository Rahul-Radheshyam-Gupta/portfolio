from django.db import models
import uuid
# Create your models here.

class Visitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=20)
    message = models.TextField(max_length=2000,null=True,blank=True)
    hr = models.BooleanField(default=False)

    def __str__(self):
        return 'visitor is '+ self.name
        
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    sem = models.CharField(max_length=10, null=True,blank=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    languages = models.CharField(max_length=20,null=True,blank=True)
    link = models.CharField(max_length=150,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return 'project is '+self.name
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url


class MyCv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cv = models.FileField(null=True)