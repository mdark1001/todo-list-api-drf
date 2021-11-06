"""
@author: mdark1001
@date: 11/06/2021
"""
from django.db import models
from django.conf import settings
from slugify import slugify

class TaskCompled(models.Manager):
    """Manager for exclusive complete tasks """
    def get_queryset(self):
        return super(TaskCompled,self).get_queryset().filter(completed=True)


class Task(models.Model):
    """Model for register user tasks  """   
    name = models.CharField(
        max_length=120,
    )
    slug = models.SlugField(

    )
    planned = models.DateField(

    )
    priority = models.SmallIntegerField(default=0)

    completed = models.BooleanField(default=False)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    # Managers 
    objects = models.Manager()
    task_compled = TaskCompled()

    def save(self, *args, **kwargs):
        """Overrite for slugname """
        if not self.slug:
            self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)
