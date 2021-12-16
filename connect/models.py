from django.db import models
from django.utils import timezone
from accounts.models import User
# Create your models here.

class Post(models.Model):
    
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    

    

class Offer(models.Model):
    owner_id = models.ManyToManyField(User , related_name="user_offer")
    to_company = models.ManyToManyField(User, related_name="companies")
    created_at = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length=255, default="title", blank=True)
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(max_length=32, default="pending", blank=True)

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    on_post = models.ManyToManyField(Post, related_name="comments")


class Activity(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, related_name="post")
    type_of_activity = models.CharField(max_length=32,default=None, blank = True)
    created_at = models.DateTimeField(default = timezone.now)



