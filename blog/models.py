from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # django enumeration for status
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    #  many-to-one relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # auto_now_add automatically stores the current date when the object is created
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add automatically stores the current date when the object is updated
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # defines the Meta data for this model
    class Meta:
        ordering = ['-publish'] # data will be ordered by the publishing dae
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title