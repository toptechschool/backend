from django.db import models
from django.utils import timezone
from django.urls import reverse 
from users.models import User
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Blog(models.Model):
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

    liked_by = models.ManyToManyField(User,related_name="BlogLikedBy")
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail-update', kwargs={'slug': self.slug})

    def get_liked_count(self):
        return self.liked_by.count()

def create_slug(instance,new_slug = None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    
pre_save.connect(pre_save_post_receiver, sender=Blog)