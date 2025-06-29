from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Note(models.Model):

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



    


