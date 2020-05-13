from django.db import models
from django.db import models 


# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200) 
    address = models.TextField() 
    email = models.CharField(max_length=400) 
    date = models.DateTimeField('Date published')
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.IntegerField(default=1) 
    
    class Meta: 
        ordering = ('-date',) 
        get_latest_by = 'date' 
        
    def __unicode__(self): 
        return u'%s' %(self.title) 
    def get_absolute_url(self): 
        return "/link/%s/" %(self.id) 

# Create your models here.
