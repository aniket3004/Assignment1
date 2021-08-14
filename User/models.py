from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name

class Post(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def  __str__(self):
        return self.text
