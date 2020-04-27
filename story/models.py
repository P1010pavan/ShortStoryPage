from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class upload(models.Model):
    Your_Name = models.CharField(max_length=50)
    Title_of_the_story = models.CharField(max_length=200)
    Date = models.DateField(auto_now=True)
    Story_Description=models.TextField(null=True)
    Image = models.ImageField(upload_to='story/',default="")
    email = models.EmailField(default="")

    def __str__(self):
        return self.Your_Name


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="")
    message = models.TextField(null=True)

    def __str__(self):
        return self.name