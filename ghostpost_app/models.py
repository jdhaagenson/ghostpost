from django.utils import timezone
from django.db import models


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

    def __str__(self):
        return self.is_boast

    @property
    def score(self):
        score = 0
        score += self.upvotes
        score -= self.downvotes
        return score
