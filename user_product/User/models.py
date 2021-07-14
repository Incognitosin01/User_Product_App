from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.
# USER MODEL IS BEEN NOT CREATED AS REQUIREMENT SUITS PERFECTLY WITH DJANGO INBUILT USER

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False,help_text="User post relation key")
    text = models.TextField(verbose_name="Post Text",help_text="Description about post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return f"{self.user}"
