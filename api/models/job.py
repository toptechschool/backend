from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.timesince import timesince
from datetime import datetime
from taggit.managers import TaggableManager
from users.models import User
from api.models import Company
from api.models.choices import CITY_CHOICES,JOB_TYPE_CHOICES


class Job(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(Company ,on_delete=models.SET_NULL,blank=True, null=True)
    location = models.IntegerField(choices=CITY_CHOICES,default=1)
    title = models.CharField(max_length=300)
    description = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    job_type = models.IntegerField(choices=JOB_TYPE_CHOICES,default=1)
    posted_at = models.DateTimeField(default=timezone.now)
    salary = models.IntegerField( 
        validators=[
            MaxValueValidator(500),
            MinValueValidator(0)
        ],
        default=0, help_text="Please put hourly salary, if unpaid leave it blank.",blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    note = models.CharField(max_length=100,blank=True, null=True)
    external_resource = models.BooleanField(default=False)
    apply_link = models.URLField(null=True,blank=True,help_text="Redirect to origin site if wanted")

    technologies = TaggableManager()
    favourite = models.ManyToManyField(User,related_name="JobFavourite")

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title
    
    def get_location(self):
        return dict(CITY_CHOICES)[self.location]

    def get_posted_at_day(self):
        time_difference = timesince(self.posted_at.date(),datetime.now().date()) 
        return time_difference+ " ago"

    def get_salary(self):
        return str(self.salary)+"$/h"

    def get_absolute_url(self):
        return reverse('job-detail-update', kwargs={'job_id': self.id})