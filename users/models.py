from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from time import time
from django_resized import ResizedImageField
from users.manager import UserManager
from django.contrib.sites.models import Site


class User(AbstractBaseUser, PermissionsMixin):
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    username = models.SlugField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'Username {self.email}'

    def save(self, *args, **kwargs):
        if self.pk is None:
            strtime = "".join(str(time()).split(".")[1])
            string = "%s%s" % (self.email.split("@")[0],strtime[:3])
            self.username = slugify(string)
            super(User, self).save()
        else:
            super(User,self).save()


USER_TYPE_CHOICES = (
    (1, 'Recruiter'),
    (2, 'Candidate'),
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email_varified = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200,null=True,blank=True)
    profile_pic = ResizedImageField(size=[1920, 1080], upload_to='profile_pics', default='default-profile.png')
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=2)

    def save(self,*args,**kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.profile_pic != self.profile_pic and this.profile_pic.name != 'default-profile.png': 
                this.profile_pic.delete(save=False)
        except: pass
        super(Profile,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.user.email}s Profile'

    @property
    def get_avatar(self):
        return self.profile_pic.url


