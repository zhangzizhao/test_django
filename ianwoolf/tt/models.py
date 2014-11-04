from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class people(models.Model):
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    Email=models.EmailField()
    create_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
#    class Admin:
#        list_display = (city, name)
#    def __str__(self):
#        if self.state:
#            return "%s %s %s" %(self.name,self.sex,self.city)
    def __unicode__(self):
        return smart_unicode(self.name)
        #return str(self.name)
