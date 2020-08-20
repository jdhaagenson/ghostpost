import datetime
from django.db import models


# Create your models here.
class Post(models.Model):
    BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))
    is_boast = models.BooleanField(choices=BOOL_CHOICES)
    content = models.CharField(max_length=250)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now,
                                blank=True,
                                null=True
                                )

    def __str__(self):
        return self.content

    @property
    def score(self):
        return self.upvotes - self.downvotes
