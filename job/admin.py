from django.contrib import admin

# Register your models here.

from .import models

admin.site.register(models.Job)
admin.site.register(models.Apply)
admin.site.register(models.Category)