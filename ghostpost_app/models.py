from django.db import models


# Create your models here.
class Post(models.Model):
    is_boast = models.BooleanField()
    content = models.CharField(max_length=250)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    date = models.DateTimeField()
