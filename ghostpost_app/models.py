from django.utils import timezone
from django.db import models
from django.utils.crypto import get_random_string
import string


# Create your models here.
class Post(models.Model):
    BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))
    is_boast = models.BooleanField(choices=BOOL_CHOICES)
    content = models.CharField(max_length=250)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now,
                                blank=True,
                                null=True
                                )
    secret = models.CharField(max_length=6,
                              unique=True)

    def __str__(self):
        return self.is_boast

    @property
    def score(self):
        return self.upvotes - self.downvotes
