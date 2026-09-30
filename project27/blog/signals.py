from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog
@receiver(pre_save,sender='blog.Blog')
def pre_save_blog(sender,instance,**kwargs):
    print("pre save signal called before saving the instance in database")
    print(instance.title)
    print(instance.content)

@receiver(post_save,sender='blog.Blog')
def post_save_blog(sender,instance,created,**kwargs):
    print("post save signal called after saving the instance in database")
    print(instance.title)
    print(instance.content)
    print("created instance:", created)
