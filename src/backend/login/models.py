from django.db import models
from django.db import models 
from .storage import DjangoUserMixin, DjangoAssociationMixin, \
                     DjangoNonceMixin, DjangoCodeMixin, \
                     DjangoPartialMixin, BaseDjangoStorage


# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200) 
    email = models.EmailField() 
    location = models.CharField(max_length=400) 
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
class DjangoStorage(BaseDjangoStorage):
    user = UserSocialAuth
    nonce = Nonce
    association = Association
    code = Code
    partial = Partial

    @classmethod
    def is_integrity_error(cls, exception):
        return exception.__class__ is IntegrityError