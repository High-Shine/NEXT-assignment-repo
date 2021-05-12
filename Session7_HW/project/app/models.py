from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    duedate = models.TextField(null=True,default='')

    def __str__(self):
        return self.title

