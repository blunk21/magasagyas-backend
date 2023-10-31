from django.db import models

# Create your models here.
class ModuleMessages(models.Model):
    id = models.AutoField(primary_key=True)

    data = models.TextField(null=False,blank=False)

    server_timestamp = models.TimeField(auto_now_add=True,null=False,blank=False)

    timestamp = models.DateTimeField(null=False,blank=False)

    class Meta:
        managed = False
        db_table = "messages"