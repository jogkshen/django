from django.contrib import admin
from selfapp import models

# Register your models here.
admin.site.register(models.person)
admin.site.register(models.registered_user)
