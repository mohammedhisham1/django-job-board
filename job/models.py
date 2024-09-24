from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)


def image_upload (instance,filename):
    imageName,extantion = filename.split('.')
    return "jobs/%s.%s"%(instance.title,extantion)

class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description =models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    job = models.ForeignKey(Job, related_name='apply_job',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
