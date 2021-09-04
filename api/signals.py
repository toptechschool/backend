from django.db.models.signals import pre_save
from django.dispatch import receiver
from api.models import Note
from api.utils import get_read_time
from django.utils.text import slugify
import uuid


def create_slug(instance):
    slug = slugify(instance.title)
    uid = uuid.uuid4()
    slug = "%s-%s" % (slug,uid.hex[:6])
    qs = Note.objects.filter(slug=slug).order_by("-id")
    if qs.exists():
        return create_slug(instance)
    return slug


@receiver(pre_save,sender=Note)
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    
    if instance.content:
        html_string = instance.content
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var