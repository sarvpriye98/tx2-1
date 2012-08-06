from django.db import models
from django.contrib.contenttypes.models import ContentType
from tx2.Security.models import SecurityStates,SecurityPermissions
from tx2.Users.models import User

# Create your models here.

class RegisterUser(models.Model):
	ContentType = models.ForeignKey(ContentType)
	Record = models.IntegerField()
	Users = models.TextField()
	Desc = models.CharField(max_length=1000)
	MetaInfo = models.CharField(max_length=2000)
	State = models.ForeignKey(SecurityStates)
	
class RegisterUserLogs(models.Model):
    # user making changes
    LogsUser = models.ForeignKey(User)
    
    ContentType = models.ForeignKey(ContentType)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPermission = models.ForeignKey(SecurityPermissions)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)

