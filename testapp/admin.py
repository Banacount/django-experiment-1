from django.contrib import admin
from .models import YourGoals, UniversalChat

# Register your models here.
admin.site.register([YourGoals, UniversalChat])
