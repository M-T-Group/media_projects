from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Model):
    photo = models.ImageField()
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return f'Owned by {self.owner.username}'
