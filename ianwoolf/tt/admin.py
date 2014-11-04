from django.contrib import admin

# Register your models here.
from .models import people

class peopleAdmin(admin.ModelAdmin):
    class Meta:
        model = people
admin.site.register(people,peopleAdmin)
