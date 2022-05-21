from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
from users.models import User
from django.utils.text import slugify


class Company(models.Model):
    '''
        Anyone should be able to create company.
        Admin will varify the status of the company after request.
    '''
    admin = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    varified = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    logo = ResizedImageField(size=[200, 200], upload_to='company_logo',force_format='PNG',default='post.jpg')
    last_updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    locations = models.CharField(max_length=200)
    website = models.URLField()
    jobs = models.URLField()
    twitter_link = models.URLField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)
    
    follower = models.ManyToManyField(User,related_name='follower',blank=True)

    class Meta:
        ordering = ['?']
        
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Company,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company-detail-update', kwargs={'slug': self.slug})