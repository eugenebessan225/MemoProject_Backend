from django.db import models
from django.contrib.auth.models import User
from . import choices


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='person')
    avatar = models.ImageField(upload_to='avatar', default='avatar/avatar.png')
    about_user = models.TextField(null=True)

    def __str__(self):
        return self.user.last_name+" "+self.user.first_name



class Book(models.Model):
    owner = models.ForeignKey(Person, related_name='Books', on_delete=models.CASCADE)
    level = models.CharField(max_length=50, choices=choices.LEVELS)
    field = models.CharField(max_length=50, choices=choices.FIELDS)
    title = models.CharField(max_length=200, null=True)
    abstract = models.TextField(null=True)
    image = models.ImageField(upload_to='guard_pages', default='guard_pages/default.jpg')
    file = models.FileField(upload_to='docs/')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    download_nb = models.IntegerField(default=0)

    def __str__(self):
        return self.title