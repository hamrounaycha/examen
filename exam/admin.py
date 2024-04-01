from django.contrib import admin

from .models import Course , Question , Option

# Register your models here.

admin.site.register(Course)
admin.site.register(Option)
admin.site.register(Question)


