from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=300)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='baseapp/static/img')
    body=RichTextField(blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


