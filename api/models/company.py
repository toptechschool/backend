from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
from users.models import User


class Company(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    logo = ResizedImageField(size=[200, 200], upload_to='company_logo',force_format='PNG',default='post.jpg')
    founded = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=150)
    website = models.URLField()
    jobs = models.URLField()
    facebook_link = models.URLField(null=True,blank=True)
    twitter_link = models.URLField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)
    
    follower = models.ManyToManyField(User,related_name='follower',blank=True)

    class Meta:
        ordering = ['?']
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail-update', kwargs={'slug': self.slug})

    @property
    def get_video_links(self):
        return VideoLink.objects.filter(company=self.pk)


class VideoLink(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return self.link