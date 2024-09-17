from django.contrib import admin

# Register your models here.

from .import models

admin.site.register(models.job)
admin.site.register(models.Category)