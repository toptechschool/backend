from django.db import models
from django.utils import timezone
from django_resized import ResizedImageField
from django.urls import reverse
from taggit.managers import TaggableManager
from users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    approved = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    read_time =  models.IntegerField(default=0)

    liked_by = models.ManyToManyField(User,related_name="noteLikedBy")
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail-update', kwargs={'slug': self.slug})

    def get_liked_count(self):
        return self.liked_by.count()
    
