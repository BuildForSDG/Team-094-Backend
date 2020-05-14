from django.db import models
from django.db import models 


# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200) 
    email = models.EmailField() 
    location = models.CharField(max_length=400)
    phone = models.CharField(max_length=20) 
    date = models.DateField('Date Published', auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.IntegerField(default=1) 
    
    class Meta: 
        ordering = ('-date',) 
        get_latest_by = 'date' 
    
    def __str__(self):
        return self.name
    
    def __unicode__(self): 
        return u'%s' %(self.title) 
    def get_absolute_url(self): 
        return "/link/%s/" %(self.id) 

